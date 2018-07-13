from copy import copy
from itertools import zip_longest

from lattec.exceptions import LatteVariableNamesError
from lattec.parser import Parser
from lattec.validations.base import (
    BaseListener,
    BaseState,
    BaseVisitor,
)
from lattec.validations.types import *
from lattec.validations.single_errors import (
    AdditionalArgument,
    MissingArgument,
    Redeclaration,
    UndeclaredUse,
    TypeMissMatch,
    NoSuchField,
)


class State(BaseState):
    def __init__(self):
        super().__init__()
        self.level = 0
        self.vars = {
            k: (-1, -1, v)
            for k, v in INITIAL_FEED.items()
        }
        self.vars_stack = []
        self.ret_type = LatteVoid()
        self.ret_type_stack = []
        self.context = None

    def add_var(self, name, type_, new_line):
        name = self.normalize_name(name)

        if name in self.vars:
            level, old_line, _ = self.vars[name]
            if level == self.level:
                self.errors.append(Redeclaration(name, old_line, new_line))

        self.vars[name] = (self.level, new_line, type_)

    def use_var(self, name, line):
        name = self.normalize_name(name)

        if name not in self.vars:
            self.errors.append(UndeclaredUse(name, line))
            return

        _, _, type_ = self.vars[name]

        return type_

    def level_up(self):
        self.level += 1
        self.vars_stack.append(dict(self.vars))
        self.ret_type_stack.append(self.ret_type)

    def level_down(self):
        self.level -= 1
        assert self.level >= 0
        self.vars = self.vars_stack[-1]
        self.vars_stack.pop()
        self.ret_type = self.ret_type_stack[-1]
        self.ret_type_stack.pop()

    def check_ret(self, t, line):
        if t == self.ret_type:
            return

        self.errors.append(TypeMissMatch(self.ret_type, t, line))

    def cmp_type(self, t1, t2, line):
        if t1 == t2:
            return

        self.errors.append(TypeMissMatch(t1, t2, line))

    def use_method(self, t: LatteType, method_name, line):
        methods = t.methods
        name = self.normalize_name(method_name)
        if name not in methods:
            self.errors.append(NoSuchField(t, name, line))
            return None, False

        ret_type = methods[name]
        return ret_type, isinstance(ret_type, LatteObject)


class VarUseVisitor(BaseVisitor):
    def __init__(self, state: State, listener: BaseListener):
        self.state = state
        self.listener = listener

    def visitProgram(self, ctx: Parser.ProgramContext):
        return self.visitChildren(ctx)

    def visitFnDef(self, ctx: Parser.FnDefContext):
        args = [] if ctx.argVec() is None else ctx.argVec().accept(self)
        ret = ctx.type_().accept(self)
        return LatteFunction(args, ret)

    def visitClsDef(self, ctx: Parser.ClsDefContext):
        return self.visitChildren(ctx)

    def visitArgVec(self, ctx: Parser.ArgVecContext):
        return [arg.accept(self) for arg in ctx.arg()]

    def visitArg(self, ctx: Parser.ArgContext):
        return ctx.type_().accept(self)

    def visitTNonArray(self, ctx: Parser.TNonArrayContext):
        return ctx.base_type().accept(self)

    def visitTArray(self, ctx: Parser.TArrayContext):
        t = ctx.basic_type().accept(self)
        return LatteArray(t)

    def visitTBasic(self, ctx: Parser.TBasicContext):
        return ctx.basic_type().accept(self)

    def visitTIdent(self, ctx: Parser.TIdentContext):
        name = ctx.ID()
        t = self.state.use_var(name, ctx.start.line)
        return LatteObject(t)

    def visitTInt(self, ctx: Parser.TIntContext):
        return LatteInt()

    def visitTStr(self, ctx: Parser.TStrContext):
        return LatteString()

    def visitTBool(self, ctx: Parser.TBoolContext):
        return LatteBool()

    def visitTVoid(self, ctx: Parser.TVoidContext):
        return LatteVoid()

    def visitNewObj(self, ctx:Parser.NewObjContext):
        t = self.state.use_var(ctx.class_name, ctx.start.line)
        if isinstance(t, LatteClass):
            return LatteObject(t)
        else:
            raise NotImplementedError()

    def visitNewObjArray(self, ctx:Parser.NewObjArrayContext):
        return self.visitChildren(ctx)

    def visitNewBasicTypeArray(self, ctx:Parser.NewBasicTypeArrayContext):
        t = ctx.basic_type().accept(self)
        return LatteArray(t)

    def visitItem(self, ctx: Parser.ItemContext):
        return self.visitChildren(ctx)

    def visitEId(self, ctx: Parser.EIdContext):
        return self.state.use_var(ctx.ID(), ctx.start.line)

    def visitEFunCall(self, ctx: Parser.EFunCallContext, t=None):
        if t is None:
            t = self.state.use_var(ctx.name, ctx.start.line)

        func_name = State.normalize_name(ctx.name)

        args = [
            arg.accept(self)
            for arg in ctx.expr()
        ]

        for expected, got, arg in zip_longest(t.args, args, ctx.expr()):
            if arg is None:
                self.state.errors.append(MissingArgument(func_name, expected, ctx.start.line))
            elif expected is None:
                self.state.errors.append(AdditionalArgument(func_name, arg.getText(), arg.start.line))
            else:
                self.state.cmp_type(expected, got, arg.start.line)

        return t.ret

    def visitERelOp(self, ctx: Parser.ERelOpContext):
        t1 = ctx.lhs.accept(self)
        t2 = ctx.rhs.accept(self)

        # TODO: cmp strings?
        self.state.cmp_type(t1, t2, ctx.start.line)

        return LatteBool()

    def visitETrue(self, ctx: Parser.ETrueContext):
        return LatteBool()

    def visitECast(self, ctx: Parser.ECastContext):
        # Should work only for null or the same type
        expr_type = ctx.expr().accept(self)
        cast_type = self.state.use_var(ctx.name, ctx.start.line)

        if not isinstance(cast_type, LatteClass):
            raise NotImplementedError('Should be a class')

        if not isinstance(expr_type, (LatteNull, LatteObject)):
            raise NotImplementedError('Should be a null or object')

        return LatteObject(cast_type)

    def visitEOr(self, ctx: Parser.EOrContext):
        t1 = ctx.lhs.accept(self)
        t2 = ctx.rhs.accept(self)

        self.state.cmp_type(LatteBool(), t1, ctx.lhs.start.line)
        self.state.cmp_type(LatteBool(), t2, ctx.rhs.start.line)

        return LatteBool()

    def visitEInt(self, ctx: Parser.EIntContext):
        return LatteInt()

    def visitEUnOp(self, ctx: Parser.EUnOpContext):
        t = ctx.expr().accept(self)

        if ctx.NOT() is not None:
            self.state.cmp_type(LatteBool(), t, ctx.start.line)
        elif ctx.SUB() is not None:
            self.state.cmp_type(LatteInt(), t, ctx.start.line)
        else:
            raise NotImplementedError()

        return t

    def visitEStr(self, ctx: Parser.EStrContext):
        return LatteString()

    def visitEMulOp(self, ctx: Parser.EMulOpContext):
        t1 = ctx.lhs.accept(self)
        t2 = ctx.rhs.accept(self)

        self.state.cmp_type(t1, t2, ctx.start.line)
        self.state.cmp_type(t1, LatteInt(), ctx.start.line)

        return LatteInt()

    def visitEAnd(self, ctx: Parser.EAndContext):
        t1 = ctx.lhs.accept(self)
        t2 = ctx.rhs.accept(self)

        self.state.cmp_type(LatteBool(), t1, ctx.lhs.start.line)
        self.state.cmp_type(LatteBool(), t2, ctx.rhs.start.line)

        return LatteBool()

    def visitEParen(self, ctx: Parser.EParenContext):
        return ctx.expr().accept(self)

    def visitEFalse(self, ctx: Parser.EFalseContext):
        return LatteBool()

    def visitENew(self, ctx: Parser.ENewContext):
        return ctx.new_expr_type().accept(self)

    def visitEAddOp(self, ctx: Parser.EAddOpContext):
        t1 = ctx.lhs.accept(self)
        t2 = ctx.rhs.accept(self)

        self.state.cmp_type(t1, t2, ctx.start.line)

        if t1.__class__ not in [LatteInt, LatteString]:
            self.state.cmp_type(t1, LatteInt(), ctx.start.line)

        return t1

    def visitEAcc(self, ctx: Parser.EAccContext, t=None):
        if t is None:
            t = ctx.obj.accept(self)
            if t is None:
                return None
            return self.visitEAcc(ctx, t)
        else:
            field = ctx.field
            if isinstance(field, Parser.EFunCallContext):
                name = field.ID()
                field_type, success = self.state.use_method(t, name, ctx.start.line)
                fn_type = self.visitEFunCall(ctx.field, field_type)
                if not success or (not isinstance(field, Parser.EAccContext)):
                    return fn_type
                return self.visitEAcc(field, fn_type)
            elif isinstance(field, Parser.EIdContext):
                name = field.ID()
                field_type, success = self.state.use_method(t, name, ctx.start.line)
                if not success or (not isinstance(field, Parser.EAccContext)):
                    return field_type
                return self.visitEAcc(field, field_type)
            elif isinstance(field, Parser.EAccContext):
                sub = copy(ctx)
                sub.field = sub.field.obj
                ret_sub = self.visitEAcc(sub, t)
                if ret_sub is None:
                    return
                return self.visitEAcc(ctx.field, ret_sub)
            else:
                raise NotImplementedError()

    def visitENull(self, ctx: Parser.ENullContext):
        return LatteNull()

    def visitEAccArr(self, ctx: Parser.EAccArrContext):
        t1 = ctx.expr()[0].accept(self)
        t2 = ctx.expr()[1].accept(self)

        self.state.cmp_type(LatteInt(), t2, ctx.expr()[1].start.line)

        return t1.t


class VarUseListener(BaseListener):
    def __init__(self):
        self.state = State()
        self.visitor = VarUseVisitor(self.state, self)

    def summarize(self):
        if self.state.errors:
            raise LatteVariableNamesError(self.state.errors)

    def enterProgram(self, ctx: Parser.ProgramContext):
        self.state.level_up()

        for topDef in ctx.topDef():
            if isinstance(topDef, Parser.ClsDefContext):
                fields = {}
                t = LatteClass(topDef.name.text, fields)
                self.state.add_var(topDef.name, t, topDef.start.line)

        self.state.level_up()

        for topDef in ctx.topDef():
            if isinstance(topDef, Parser.FnDefContext):
                fn = topDef.accept(self.visitor)
                self.state.add_var(topDef.name, fn, topDef.start.line)
            elif isinstance(topDef, Parser.ClsDefContext):
                fields = {}
                for field in topDef.clsElem():
                    if isinstance(field, Parser.FieldContext):
                        name = field.ID().getText()
                        t = field.type_().accept(self.visitor)
                    elif isinstance(field, Parser.MethodContext):
                        name = State.normalize_name(field.topDef().name)
                        t = field.topDef().accept(self.visitor)
                    else:
                        raise NotImplementedError()

                    if name in fields:
                        raise NotImplementedError()

                    fields[name] = t

                t = self.state.use_var(topDef.name, topDef.start.line)
                t.fields = fields

        self.state.level_up()

        for topDef in ctx.topDef():
            topDef.enterRule(self)

        self.state.level_down()
        self.state.level_down()
        self.state.level_down()

    def enterFnDef(self, ctx: Parser.FnDefContext):
        self.state.level_up()

        if ctx.argVec() is not None:
            ctx.argVec().enterRule(self)

        t = ctx.type_().accept(self.visitor)
        self.state.ret_type = t

        ctx.block().enterRule(self)

        self.state.level_down()

    def enterClsDef(self, ctx: Parser.ClsDefContext):
        self.state.level_up()
        self.state.context = ctx.name

        t = self.state.use_var(ctx.name, ctx.start.line)

        if isinstance(t, LatteClass):
            self.state.add_var('self', LatteObject(t), ctx.start.line)
            for name, sub_t in t.fields.items():
                self.state.add_var(name, sub_t, ctx.start.line)

        else:
            raise NotImplementedError()

        self.state.level_up()

        for field in ctx.clsElem():
            if isinstance(field, Parser.FieldContext):
                pass
            elif isinstance(field, Parser.MethodContext):
                field.topDef().enterRule(self)
            else:
                raise NotImplementedError()

        self.state.context = None
        self.state.level_down()
        self.state.level_down()

    def enterArgVec(self, ctx: Parser.ArgVecContext):
        for arg in ctx.arg():
            arg.enterRule(self)

    def enterArg(self, ctx: Parser.ArgContext):
        t = ctx.accept(self.visitor)
        self.state.add_var(ctx.name, t, ctx.start.line)

    def enterBlock(self, ctx: Parser.BlockContext):
        self.state.level_up()

        for stmt in ctx.stmt():
            stmt.enterRule(self)

        self.state.level_down()

    def enterEmpty(self, ctx: Parser.EmptyContext):
        pass

    def enterBlockStmt(self, ctx: Parser.BlockStmtContext):
        ctx.block().enterRule(self)

    def enterDecl(self, ctx: Parser.DeclContext):
        for item in ctx.item():
            item.enterRule(self)

    def enterAss(self, ctx: Parser.AssContext):
        t1 = ctx.target.accept(self.visitor)
        t2 = ctx.value.accept(self.visitor)

        self.state.cmp_type(t1, t2, ctx.start.line)

    def enterIncr(self, ctx: Parser.IncrContext):
        t = self.state.use_var(ctx.name, ctx.start.line)
        self.state.cmp_type(LatteInt(), t, ctx.start.line)

    def enterDecr(self, ctx: Parser.DecrContext):
        t = self.state.use_var(ctx.name, ctx.start.line)
        self.state.cmp_type(LatteInt(), t, ctx.start.line)

    def enterRet(self, ctx: Parser.RetContext):
        t = ctx.expr().accept(self.visitor)
        self.state.check_ret(t, ctx.start.line)

    def enterVRet(self, ctx: Parser.VRetContext):
        self.state.check_ret(LatteVoid(), ctx.start.line)

    def enterCond(self, ctx: Parser.CondContext):
        t = ctx.cond.accept(self.visitor)
        self.state.cmp_type(t, LatteBool(), ctx.start.line)

        self.state.level_up()
        ctx.true_stmt.enterRule(self)
        self.state.level_down()

    def enterCondElse(self, ctx: Parser.CondElseContext):
        t = ctx.cond.accept(self.visitor)
        self.state.cmp_type(t, LatteBool(), ctx.start.line)

        self.state.level_up()
        ctx.true_stmt.enterRule(self)
        self.state.level_down()

        self.state.level_up()
        ctx.false_stmt.enterRule(self)
        self.state.level_down()

    def enterWhile(self, ctx: Parser.WhileContext):
        t = ctx.cond.accept(self.visitor)
        self.state.cmp_type(t, LatteBool(), ctx.start.line)

        self.state.level_up()
        ctx.true_stmt.enterRule(self)
        self.state.level_down()

    def enterForEach(self, ctx: Parser.ForEachContext):
        self.state.level_up()

        arr_type = ctx.expr().accept(self.visitor)
        var_type = ctx.type_().accept(self.visitor)

        self.state.cmp_type(LatteArray(var_type), arr_type, ctx.start.line)
        self.state.add_var(ctx.name, var_type, ctx.start.line)

        self.state.level_up()

        ctx.stmt().enterRule(self)

        self.state.level_down()

        self.state.level_down()

    def enterSExp(self, ctx: Parser.SExpContext):
        ctx.expr().accept(self.visitor)

    def enterItem(self, ctx: Parser.ItemContext):
        # ugly
        t = ctx.parentCtx.type_().accept(self.visitor)

        if ctx.expr() is not None:
            expr_t = ctx.expr().accept(self.visitor)
            self.state.cmp_type(t, expr_t, ctx.start.line)

        self.state.add_var(ctx.name, t, ctx.start.line)

from lattec.parser import Parser
from lattec.validations.base import (
    BaseListener,
    BaseVisitor,
)
from lattec.validations.types import *
from lattec.validations.single_errors import (
    Redeclaration,
    UndeclaredUse,
)


class State:
    def __init__(self):
        self.level = 0
        self.vars = {}
        self.errors = []
        self.vars_stack = []
        self.ret_type = LatteVoid()
        self.ret_type_stack = []

    def add_var(self, name, type_, new_line):
        if name in self.vars:
            level, old_line, _ = self.vars[name]
            if level == self.level:
                self.errors.append(Redeclaration(name, old_line, new_line))

        self.vars[name] = (self.level, new_line, type_)

    def use_var(self, name, line):
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

    def check_ret(self, t):
        if t == self.ret_type:
            return

        raise NotImplementedError()

    def cmp_type(self, t1, t2):
        if t1 == t2:
            return

        raise NotImplementedError()


class VarUseVisitor(BaseVisitor):
    def __init__(self, state):
        self.state = state

    def visitProgram(self, ctx: Parser.ProgramContext):
        return self.visitChildren(ctx)

    def visitFnDef(self, ctx: Parser.FnDefContext):
        return self.visitChildren(ctx)

    def visitClsDef(self, ctx: Parser.ClsDefContext):
        return self.visitChildren(ctx)

    def visitArgVec(self, ctx: Parser.ArgVecContext):
        return [arg.accept(self) for arg in ctx.arg()]

    def visitArg(self, ctx: Parser.ArgContext):
        return ctx.type_().accept(self)

    def visitBlock(self, ctx: Parser.BlockContext):
        return self.visitChildren(ctx)

    def visitField(self, ctx: Parser.FieldContext):
        return self.visitChildren(ctx)

    def visitMethod(self, ctx: Parser.MethodContext):
        return self.visitChildren(ctx)

    def visitEmpty(self, ctx: Parser.EmptyContext):
        return self.visitChildren(ctx)

    def visitBlockStmt(self, ctx: Parser.BlockStmtContext):
        return self.visitChildren(ctx)

    def visitDecl(self, ctx: Parser.DeclContext):
        return self.visitChildren(ctx)

    def visitAss(self, ctx: Parser.AssContext):
        return self.visitChildren(ctx)

    def visitIncr(self, ctx: Parser.IncrContext):
        return self.visitChildren(ctx)

    def visitDecr(self, ctx: Parser.DecrContext):
        return self.visitChildren(ctx)

    def visitRet(self, ctx: Parser.RetContext):
        return self.visitChildren(ctx)

    def visitVRet(self, ctx: Parser.VRetContext):
        return self.visitChildren(ctx)

    def visitCond(self, ctx: Parser.CondContext):
        return self.visitChildren(ctx)

    def visitCondElse(self, ctx: Parser.CondElseContext):
        return self.visitChildren(ctx)

    def visitWhile(self, ctx: Parser.WhileContext):
        return self.visitChildren(ctx)

    def visitForEach(self, ctx: Parser.ForEachContext):
        return self.visitChildren(ctx)

    def visitSExp(self, ctx: Parser.SExpContext):
        return self.visitChildren(ctx)

    def visitArrAcc(self, ctx: Parser.ArrAccContext):
        return self.visitChildren(ctx)

    def visitIdentVec(self, ctx: Parser.IdentVecContext):
        return self.visitChildren(ctx)

    def visitTNonArray(self, ctx: Parser.TNonArrayContext):
        return ctx.base_type().accept(self)

    def visitTArray(self, ctx: Parser.TArrayContext):
        return self.visitChildren(ctx)

    def visitTBasic(self, ctx: Parser.TBasicContext):
        return ctx.basic_type().accept(self)

    def visitTIdent(self, ctx: Parser.TIdentContext):
        return self.visitChildren(ctx)

    def visitTInt(self, ctx: Parser.TIntContext):
        return LatteInt()

    def visitTStr(self, ctx: Parser.TStrContext):
        return LatteString()

    def visitTBool(self, ctx: Parser.TBoolContext):
        return LatteBool()

    def visitTVoid(self, ctx: Parser.TVoidContext):
        return LatteVoid()

    def visitNew_expr_type(self, ctx: Parser.New_expr_typeContext):
        return self.visitChildren(ctx)

    def visitItem(self, ctx: Parser.ItemContext):
        return self.visitChildren(ctx)

    def visitEId(self, ctx: Parser.EIdContext):
        return self.visitChildren(ctx)

    def visitEFunCall(self, ctx: Parser.EFunCallContext):
        return self.visitChildren(ctx)

    def visitERelOp(self, ctx: Parser.ERelOpContext):
        return self.visitChildren(ctx)

    def visitETrue(self, ctx: Parser.ETrueContext):
        return LatteBool()

    def visitECast(self, ctx: Parser.ECastContext):
        return self.visitChildren(ctx)

    def visitEOr(self, ctx: Parser.EOrContext):
        return self.visitChildren(ctx)

    def visitEInt(self, ctx: Parser.EIntContext):
        return LatteInt()

    def visitEUnOp(self, ctx: Parser.EUnOpContext):
        return self.visitChildren(ctx)

    def visitEStr(self, ctx: Parser.EStrContext):
        return self.visitChildren(ctx)

    def visitEMulOp(self, ctx: Parser.EMulOpContext):
        return self.visitChildren(ctx)

    def visitEAnd(self, ctx: Parser.EAndContext):
        return self.visitChildren(ctx)

    def visitEParen(self, ctx: Parser.EParenContext):
        return self.visitChildren(ctx)

    def visitEFalse(self, ctx: Parser.EFalseContext):
        return LatteBool()

    def visitENew(self, ctx: Parser.ENewContext):
        return self.visitChildren(ctx)

    def visitEAddOp(self, ctx: Parser.EAddOpContext):
        return self.visitChildren(ctx)

    def visitEAcc(self, ctx: Parser.EAccContext):
        return self.visitChildren(ctx)

    def visitENull(self, ctx: Parser.ENullContext):
        return self.visitChildren(ctx)

    def visitEAccArr(self, ctx: Parser.EAccArrContext):
        return self.visitChildren(ctx)

    def visitAddOp(self, ctx: Parser.AddOpContext):
        return self.visitChildren(ctx)

    def visitMulOp(self, ctx: Parser.MulOpContext):
        return self.visitChildren(ctx)

    def visitRelOp(self, ctx: Parser.RelOpContext):
        return self.visitChildren(ctx)



class VarUseListener(BaseListener):
    def __init__(self):
        self.state = State()
        self.visitor = VarUseVisitor(self.state)

    def summarize(self):
        if self.state.errors:
            raise NotImplementedError()

    def enterProgram(self, ctx: Parser.ProgramContext):
        self.state.level_up()

        for topDef in ctx.topDef():
            if isinstance(topDef, Parser.FnDefContext):
                args = [] if topDef.argVec() is None else topDef.argVec().accept(self.visitor)
                ret = topDef.type_().accept(self.visitor)
                fn = LatteFunction(args, ret)
                self.state.add_var(topDef.name, fn, topDef.start.line)

        self.state.level_up()

        for topDef in ctx.topDef():
            topDef.enterRule(self)

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
        raise NotImplementedError()

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

    def enterField(self, ctx: Parser.FieldContext):
        raise NotImplementedError()

    def enterMethod(self, ctx: Parser.MethodContext):
        raise NotImplementedError()

    def enterEmpty(self, ctx: Parser.EmptyContext):
        raise NotImplementedError()

    def enterBlockStmt(self, ctx: Parser.BlockStmtContext):
        raise NotImplementedError()

    def enterDecl(self, ctx: Parser.DeclContext):
        for item in ctx.item():
            item.enterRule(self)

    def enterAss(self, ctx: Parser.AssContext):
        raise NotImplementedError()

    def enterIncr(self, ctx: Parser.IncrContext):
        raise NotImplementedError()

    def enterDecr(self, ctx: Parser.DecrContext):
        raise NotImplementedError()

    def enterRet(self, ctx: Parser.RetContext):
        t = ctx.expr().accept(self.visitor)
        self.state.check_ret(t)

    def enterVRet(self, ctx: Parser.VRetContext):
        self.state.check_ret(LatteVoid())

    def enterCond(self, ctx: Parser.CondContext):
        raise NotImplementedError()

    def enterCondElse(self, ctx: Parser.CondElseContext):
        raise NotImplementedError()

    def enterWhile(self, ctx: Parser.WhileContext):
        raise NotImplementedError()

    def enterForEach(self, ctx: Parser.ForEachContext):
        raise NotImplementedError()

    def enterSExp(self, ctx: Parser.SExpContext):
        raise NotImplementedError()

    def enterArrAcc(self, ctx: Parser.ArrAccContext):
        raise NotImplementedError()

    def enterIdentVec(self, ctx: Parser.IdentVecContext):
        raise NotImplementedError()

    def enterTNonArray(self, ctx: Parser.TNonArrayContext):
        raise NotImplementedError()

    def enterTArray(self, ctx: Parser.TArrayContext):
        raise NotImplementedError()

    def enterTBasic(self, ctx: Parser.TBasicContext):
        raise NotImplementedError()

    def enterTIdent(self, ctx: Parser.TIdentContext):
        raise NotImplementedError()

    def enterTInt(self, ctx: Parser.TIntContext):
        raise NotImplementedError()

    def enterTStr(self, ctx: Parser.TStrContext):
        raise NotImplementedError()

    def enterTBool(self, ctx: Parser.TBoolContext):
        raise NotImplementedError()

    def enterTVoid(self, ctx: Parser.TVoidContext):
        raise NotImplementedError()

    def enterNew_expr_type(self, ctx: Parser.New_expr_typeContext):
        raise NotImplementedError()

    def enterItem(self, ctx: Parser.ItemContext):
        # ugly
        t = ctx.parentCtx.type_().accept(self.visitor)

        if ctx.expr() is not None:
            expr_t = ctx.expr().accept(self.visitor)
            self.state.cmp_type(t, expr_t)

        self.state.add_var(ctx.name, t, ctx.start.line)

    def enterEId(self, ctx: Parser.EIdContext):
        raise NotImplementedError()

    def enterEFunCall(self, ctx: Parser.EFunCallContext):
        raise NotImplementedError()

    def enterERelOp(self, ctx: Parser.ERelOpContext):
        raise NotImplementedError()

    def enterETrue(self, ctx: Parser.ETrueContext):
        raise NotImplementedError()

    def enterECast(self, ctx: Parser.ECastContext):
        raise NotImplementedError()

    def enterEOr(self, ctx: Parser.EOrContext):
        raise NotImplementedError()

    def enterEInt(self, ctx: Parser.EIntContext):
        raise NotImplementedError()

    def enterEUnOp(self, ctx: Parser.EUnOpContext):
        raise NotImplementedError()

    def enterEStr(self, ctx: Parser.EStrContext):
        raise NotImplementedError()

    def enterEMulOp(self, ctx: Parser.EMulOpContext):
        raise NotImplementedError()

    def enterEAnd(self, ctx: Parser.EAndContext):
        raise NotImplementedError()

    def enterEParen(self, ctx: Parser.EParenContext):
        raise NotImplementedError()

    def enterEFalse(self, ctx: Parser.EFalseContext):
        raise NotImplementedError()

    def enterENew(self, ctx: Parser.ENewContext):
        raise NotImplementedError()

    def enterEAddOp(self, ctx: Parser.EAddOpContext):
        raise NotImplementedError()

    def enterEAcc(self, ctx: Parser.EAccContext):
        raise NotImplementedError()

    def enterENull(self, ctx: Parser.ENullContext):
        raise NotImplementedError()

    def enterEAccArr(self, ctx: Parser.EAccArrContext):
        raise NotImplementedError()

    def enterAddOp(self, ctx: Parser.AddOpContext):
        raise NotImplementedError()

    def enterMulOp(self, ctx: Parser.MulOpContext):
        raise NotImplementedError()

    def enterRelOp(self, ctx: Parser.RelOpContext):
        raise NotImplementedError()

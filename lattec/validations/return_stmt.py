from lattec.exceptions import LatteReturnError
from lattec.parser import Parser
from lattec.validations.base import (
    BaseListener,
    BaseState,
    BaseVisitor,
)
from lattec.validations.single_errors import NoReturn


class State(BaseState):
    def __init__(self):
        super().__init__()
        self.name = None
        self.line = None
        self.got_return = False

    def enter_func(self, name, line):
        self.name = self.normalize_name(name)
        self.line = line
        self.got_return = False

    def leave_func(self):
        if not self.got_return:
            self.add_error()
        self.name = None
        self.line = None

    def add_error(self):
        self.errors.append(NoReturn(self.name, self.line))


class ReturnListener(BaseListener):
    def __init__(self):
        self.state = State()
        self.visitor = ReturnVisitor(self.state)

    def summarize(self):
        if self.state.errors:
            raise LatteReturnError(self.state.errors)

    def enterProgram(self, ctx: Parser.ProgramContext):
        for topDef in ctx.topDef():
            topDef.enterRule(self)

    def enterFnDef(self, ctx: Parser.FnDefContext):
        if ctx.type_().getText() == 'void':
            return

        self.state.enter_func(ctx.name, ctx.start.line)

        ctx.block().enterRule(self)

        self.state.leave_func()

    def enterClsDef(self, ctx: Parser.ClsDefContext):
        for elem in ctx.clsElem():
            elem.enterRule(self)


    def enterBlock(self, ctx: Parser.BlockContext):
        for stmt in ctx.stmt():
            stmt.enterRule(self)

    def enterField(self, ctx: Parser.FieldContext):
        pass

    def enterMethod(self, ctx: Parser.MethodContext):
        ctx.topDef().enterRule(self)

    def enterEmpty(self, ctx: Parser.EmptyContext):
        pass

    def enterBlockStmt(self, ctx: Parser.BlockStmtContext):
        ctx.block().enterRule(self)

    def enterDecl(self, ctx: Parser.DeclContext):
        pass

    def enterAss(self, ctx: Parser.AssContext):
        pass

    def enterIncr(self, ctx: Parser.IncrContext):
        pass

    def enterDecr(self, ctx: Parser.DecrContext):
        pass

    def enterRet(self, ctx: Parser.RetContext):
        self.state.got_return = True

    def enterCond(self, ctx: Parser.CondContext):
        true_val = ctx.true_stmt.accept(self.visitor)

        if isinstance(ctx.cond, Parser.ETrueContext) and true_val:
            self.state.got_return = True

    def enterCondElse(self, ctx: Parser.CondElseContext):
        true_val = ctx.true_stmt.accept(self.visitor)
        false_val = ctx.false_stmt.accept(self.visitor)

        if isinstance(ctx.cond, Parser.ETrueContext) and true_val:
            self.state.got_return = True
        elif isinstance(ctx.cond, Parser.EFalseContext) and false_val:
            self.state.got_return = True
        elif true_val and false_val:
            self.state.got_return = True

    def enterWhile(self, ctx: Parser.WhileContext):
        true_val = ctx.true_stmt.accept(self.visitor)

        if isinstance(ctx.cond, Parser.ETrueContext) and true_val:
            self.state.got_return = True

    def enterForEach(self, ctx: Parser.ForEachContext):
        pass

    def enterSExp(self, ctx: Parser.SExpContext):
        pass


class ReturnVisitor(BaseVisitor):
    def __init__(self, state):
        self.state = state

    def visitBlock(self, ctx: Parser.BlockContext):
        return any((
            stmt.accept(self)
            for stmt in ctx.stmt()
        ))

    def visitEmpty(self, ctx: Parser.EmptyContext):
        return False

    def visitBlockStmt(self, ctx: Parser.BlockStmtContext):
        return ctx.block().accept(self)

    def visitDecl(self, ctx: Parser.DeclContext):
        return False

    def visitAss(self, ctx: Parser.AssContext):
        return False

    def visitIncr(self, ctx: Parser.IncrContext):
        return False

    def visitDecr(self, ctx: Parser.DecrContext):
        return False

    def visitRet(self, ctx: Parser.RetContext):
        return True

    def visitCond(self, ctx: Parser.CondContext):
        true_val = ctx.true_stmt.accept(self)
        return true_val and isinstance(ctx.cond, Parser.ETrueContext)

    def visitCondElse(self, ctx: Parser.CondElseContext):
        true_val = ctx.true_stmt.accept(self)
        false_val = ctx.false_stmt.accept(self)

        if isinstance(ctx.cond, Parser.ETrueContext) and true_val:
            return True
        elif isinstance(ctx.cond, Parser.EFalseContext) and false_val:
            return True
        return true_val and false_val

    def visitWhile(self, ctx: Parser.WhileContext):
        true_val = ctx.true_stmt.accept(self)
        return true_val and isinstance(ctx.cond, Parser.ETrueContext)

    def visitForEach(self, ctx: Parser.ForEachContext):
        return False

    def visitSExp(self, ctx: Parser.SExpContext):
        return False

from lattec.parser import Parser
from lattec.validations.base import (
    BaseListener,
    BaseState,
    BaseVisitor,
)


class State(BaseState):
    pass


class ReturnListener(BaseListener):
    def __init__(self):
        self.state = State()
        self.visitor = ReturnVisitor(self.state)

    def summarize(self):
        pass

    def enterProgram(self, ctx: Parser.ProgramContext):
        raise NotImplementedError()

    def enterFnDef(self, ctx: Parser.FnDefContext):
        raise NotImplementedError()

    def enterClsDef(self, ctx: Parser.ClsDefContext):
        raise NotImplementedError()

    def enterArgVec(self, ctx: Parser.ArgVecContext):
        raise NotImplementedError()

    def enterArg(self, ctx: Parser.ArgContext):
        raise NotImplementedError()

    def enterBlock(self, ctx: Parser.BlockContext):
        raise NotImplementedError()

    def enterField(self, ctx: Parser.FieldContext):
        raise NotImplementedError()

    def enterMethod(self, ctx: Parser.MethodContext):
        raise NotImplementedError()

    def enterEmpty(self, ctx: Parser.EmptyContext):
        raise NotImplementedError()

    def enterBlockStmt(self, ctx: Parser.BlockStmtContext):
        raise NotImplementedError()

    def enterDecl(self, ctx: Parser.DeclContext):
        raise NotImplementedError()

    def enterAss(self, ctx: Parser.AssContext):
        raise NotImplementedError()

    def enterIncr(self, ctx: Parser.IncrContext):
        raise NotImplementedError()

    def enterDecr(self, ctx: Parser.DecrContext):
        raise NotImplementedError()

    def enterRet(self, ctx: Parser.RetContext):
        raise NotImplementedError()

    def enterVRet(self, ctx: Parser.VRetContext):
        raise NotImplementedError()

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

    def enterNewObj(self, ctx: Parser.NewObjContext):
        raise NotImplementedError()

    def enterNewObjArray(self, ctx: Parser.NewObjArrayContext):
        raise NotImplementedError()

    def enterNewBasicTypeArray(self, ctx: Parser.NewBasicTypeArrayContext):
        raise NotImplementedError()

    def enterNew_expr_type(self, ctx: Parser.New_expr_typeContext):
        raise NotImplementedError()

    def enterItem(self, ctx: Parser.ItemContext):
        raise NotImplementedError()

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


class ReturnVisitor(BaseVisitor):
    def __init__(self, state):
        self.state = state

    def visitProgram(self, ctx: Parser.ProgramContext):
        return self.visitChildren(ctx)

    def visitFnDef(self, ctx: Parser.FnDefContext):
        return self.visitChildren(ctx)

    def visitClsDef(self, ctx: Parser.ClsDefContext):
        return self.visitChildren(ctx)

    def visitArgVec(self, ctx: Parser.ArgVecContext):
        return self.visitChildren(ctx)

    def visitArg(self, ctx: Parser.ArgContext):
        return self.visitChildren(ctx)

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

    def visitTNonArray(self, ctx: Parser.TNonArrayContext):
        return self.visitChildren(ctx)

    def visitTArray(self, ctx: Parser.TArrayContext):
        return self.visitChildren(ctx)

    def visitTBasic(self, ctx: Parser.TBasicContext):
        return self.visitChildren(ctx)

    def visitTIdent(self, ctx: Parser.TIdentContext):
        return self.visitChildren(ctx)

    def visitTInt(self, ctx: Parser.TIntContext):
        return self.visitChildren(ctx)

    def visitTStr(self, ctx: Parser.TStrContext):
        return self.visitChildren(ctx)

    def visitTBool(self, ctx: Parser.TBoolContext):
        return self.visitChildren(ctx)

    def visitTVoid(self, ctx: Parser.TVoidContext):
        return self.visitChildren(ctx)

    def visitNewObj(self, ctx: Parser.NewObjContext):
        return self.visitChildren(ctx)

    def visitNewObjArray(self, ctx: Parser.NewObjArrayContext):
        return self.visitChildren(ctx)

    def visitNewBasicTypeArray(self, ctx: Parser.NewBasicTypeArrayContext):
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
        return self.visitChildren(ctx)

    def visitECast(self, ctx: Parser.ECastContext):
        return self.visitChildren(ctx)

    def visitEOr(self, ctx: Parser.EOrContext):
        return self.visitChildren(ctx)

    def visitEInt(self, ctx: Parser.EIntContext):
        return self.visitChildren(ctx)

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
        return self.visitChildren(ctx)

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

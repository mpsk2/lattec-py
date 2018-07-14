from lattec.parser import Parser
from lattec.validations.base import BaseVisitor


class ShortenExprsVisitor(BaseVisitor):
    def visit(self, tree):
        return tree.accept(self)

    def visitChildren(self, node):
        ret = super().visitChildren(node)
        return ' '.join(ret)

    def visitTerminal(self, node):
        return node.getText()

    def visitErrorNode(self, node):
        raise ValueError(node)

    def defaultResult(self):
        return []

    def aggregateResult(self, aggregate, nextResult):
        aggregate.append(nextResult)
        return aggregate

    def shouldVisitNextChild(self, node, currentResult):
        return True

    def visitClsDef(self, ctx: Parser.ClsDefContext):
        raise NotImplementedError(ctx.__class__.__name__)

    def visitArgVec(self, ctx: Parser.ArgVecContext):
        raise NotImplementedError(ctx.__class__.__name__)

    def visitArg(self, ctx: Parser.ArgContext):
        raise NotImplementedError(ctx.__class__.__name__)

    def visitField(self, ctx: Parser.FieldContext):
        raise NotImplementedError(ctx.__class__.__name__)

    def visitMethod(self, ctx: Parser.MethodContext):
        raise NotImplementedError(ctx.__class__.__name__)

    def visitEmpty(self, ctx: Parser.EmptyContext):
        raise NotImplementedError(ctx.__class__.__name__)

    def visitBlockStmt(self, ctx: Parser.BlockStmtContext):
        raise NotImplementedError(ctx.__class__.__name__)

    def visitDecl(self, ctx: Parser.DeclContext):
        raise NotImplementedError(ctx.__class__.__name__)

    def visitAss(self, ctx: Parser.AssContext):
        raise NotImplementedError(ctx.__class__.__name__)

    def visitIncr(self, ctx: Parser.IncrContext):
        raise NotImplementedError(ctx.__class__.__name__)

    def visitDecr(self, ctx: Parser.DecrContext):
        raise NotImplementedError(ctx.__class__.__name__)

    def visitCond(self, ctx: Parser.CondContext):
        raise NotImplementedError(ctx.__class__.__name__)

    def visitCondElse(self, ctx: Parser.CondElseContext):
        raise NotImplementedError(ctx.__class__.__name__)

    def visitWhile(self, ctx: Parser.WhileContext):
        raise NotImplementedError(ctx.__class__.__name__)

    def visitForEach(self, ctx: Parser.ForEachContext):
        raise NotImplementedError(ctx.__class__.__name__)

    def visitSExp(self, ctx: Parser.SExpContext):
        raise NotImplementedError(ctx.__class__.__name__)

    def visitTArray(self, ctx: Parser.TArrayContext):
        raise NotImplementedError(ctx.__class__.__name__)

    def visitTIdent(self, ctx: Parser.TIdentContext):
        raise NotImplementedError(ctx.__class__.__name__)

    def visitNewObj(self, ctx: Parser.NewObjContext):
        raise NotImplementedError(ctx.__class__.__name__)

    def visitNewObjArray(self, ctx: Parser.NewObjArrayContext):
        raise NotImplementedError(ctx.__class__.__name__)

    def visitNewBasicTypeArray(self, ctx: Parser.NewBasicTypeArrayContext):
        raise NotImplementedError(ctx.__class__.__name__)

    def visitItem(self, ctx: Parser.ItemContext):
        raise NotImplementedError(ctx.__class__.__name__)

    def visitEId(self, ctx: Parser.EIdContext):
        raise NotImplementedError(ctx.__class__.__name__)

    def visitEFunCall(self, ctx: Parser.EFunCallContext):
        raise NotImplementedError(ctx.__class__.__name__)

    def visitERelOp(self, ctx: Parser.ERelOpContext):
        raise NotImplementedError(ctx.__class__.__name__)

    def visitETrue(self, ctx: Parser.ETrueContext):
        raise NotImplementedError(ctx.__class__.__name__)

    def visitECast(self, ctx: Parser.ECastContext):
        raise NotImplementedError(ctx.__class__.__name__)

    def visitEOr(self, ctx: Parser.EOrContext):
        raise NotImplementedError(ctx.__class__.__name__)

    def visitEInt(self, ctx: Parser.EIntContext):
        raise NotImplementedError(ctx.__class__.__name__)

    def visitEUnOp(self, ctx: Parser.EUnOpContext):
        raise NotImplementedError(ctx.__class__.__name__)

    def visitEStr(self, ctx: Parser.EStrContext):
        raise NotImplementedError(ctx.__class__.__name__)

    def visitEMulOp(self, ctx: Parser.EMulOpContext):
        raise NotImplementedError(ctx.__class__.__name__)

    def visitEAnd(self, ctx: Parser.EAndContext):
        raise NotImplementedError(ctx.__class__.__name__)

    def visitEParen(self, ctx: Parser.EParenContext):
        raise NotImplementedError(ctx.__class__.__name__)

    def visitEFalse(self, ctx: Parser.EFalseContext):
        raise NotImplementedError(ctx.__class__.__name__)

    def visitENew(self, ctx: Parser.ENewContext):
        raise NotImplementedError(ctx.__class__.__name__)

    def visitEAddOp(self, ctx: Parser.EAddOpContext):

        raise NotImplementedError(ctx.__class__.__name__)

    def visitEAcc(self, ctx: Parser.EAccContext):
        raise NotImplementedError(ctx.__class__.__name__)

    def visitENull(self, ctx: Parser.ENullContext):
        raise NotImplementedError(ctx.__class__.__name__)

    def visitEAccArr(self, ctx: Parser.EAccArrContext):
        raise NotImplementedError(ctx.__class__.__name__)

    def visitAddOp(self, ctx: Parser.AddOpContext):
        raise NotImplementedError(ctx.__class__.__name__)

    def visitMulOp(self, ctx: Parser.MulOpContext):
        raise NotImplementedError(ctx.__class__.__name__)

    def visitRelOp(self, ctx: Parser.RelOpContext):
        raise NotImplementedError(ctx.__class__.__name__)

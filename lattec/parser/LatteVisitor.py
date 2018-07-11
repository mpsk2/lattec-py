# Generated from lattec/parser/Latte.g4 by ANTLR 4.7.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .LatteParser import LatteParser
else:
    from LatteParser import LatteParser

# This class defines a complete generic visitor for a parse tree produced by LatteParser.

class LatteVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by LatteParser#program.
    def visitProgram(self, ctx:LatteParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LatteParser#FnDef.
    def visitFnDef(self, ctx:LatteParser.FnDefContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LatteParser#ClsDef.
    def visitClsDef(self, ctx:LatteParser.ClsDefContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LatteParser#argVec.
    def visitArgVec(self, ctx:LatteParser.ArgVecContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LatteParser#arg.
    def visitArg(self, ctx:LatteParser.ArgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LatteParser#block.
    def visitBlock(self, ctx:LatteParser.BlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LatteParser#Field.
    def visitField(self, ctx:LatteParser.FieldContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LatteParser#Method.
    def visitMethod(self, ctx:LatteParser.MethodContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LatteParser#Empty.
    def visitEmpty(self, ctx:LatteParser.EmptyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LatteParser#BlockStmt.
    def visitBlockStmt(self, ctx:LatteParser.BlockStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LatteParser#Decl.
    def visitDecl(self, ctx:LatteParser.DeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LatteParser#Ass.
    def visitAss(self, ctx:LatteParser.AssContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LatteParser#Incr.
    def visitIncr(self, ctx:LatteParser.IncrContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LatteParser#Decr.
    def visitDecr(self, ctx:LatteParser.DecrContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LatteParser#Ret.
    def visitRet(self, ctx:LatteParser.RetContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LatteParser#VRet.
    def visitVRet(self, ctx:LatteParser.VRetContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LatteParser#Cond.
    def visitCond(self, ctx:LatteParser.CondContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LatteParser#CondElse.
    def visitCondElse(self, ctx:LatteParser.CondElseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LatteParser#While.
    def visitWhile(self, ctx:LatteParser.WhileContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LatteParser#ForEach.
    def visitForEach(self, ctx:LatteParser.ForEachContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LatteParser#SExp.
    def visitSExp(self, ctx:LatteParser.SExpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LatteParser#TNonArray.
    def visitTNonArray(self, ctx:LatteParser.TNonArrayContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LatteParser#TArray.
    def visitTArray(self, ctx:LatteParser.TArrayContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LatteParser#TBasic.
    def visitTBasic(self, ctx:LatteParser.TBasicContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LatteParser#TIdent.
    def visitTIdent(self, ctx:LatteParser.TIdentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LatteParser#TInt.
    def visitTInt(self, ctx:LatteParser.TIntContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LatteParser#TStr.
    def visitTStr(self, ctx:LatteParser.TStrContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LatteParser#TBool.
    def visitTBool(self, ctx:LatteParser.TBoolContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LatteParser#TVoid.
    def visitTVoid(self, ctx:LatteParser.TVoidContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LatteParser#NewObj.
    def visitNewObj(self, ctx:LatteParser.NewObjContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LatteParser#NewObjArray.
    def visitNewObjArray(self, ctx:LatteParser.NewObjArrayContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LatteParser#NewBasicTypeArray.
    def visitNewBasicTypeArray(self, ctx:LatteParser.NewBasicTypeArrayContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LatteParser#item.
    def visitItem(self, ctx:LatteParser.ItemContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LatteParser#EId.
    def visitEId(self, ctx:LatteParser.EIdContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LatteParser#EFunCall.
    def visitEFunCall(self, ctx:LatteParser.EFunCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LatteParser#ERelOp.
    def visitERelOp(self, ctx:LatteParser.ERelOpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LatteParser#ETrue.
    def visitETrue(self, ctx:LatteParser.ETrueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LatteParser#ECast.
    def visitECast(self, ctx:LatteParser.ECastContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LatteParser#EOr.
    def visitEOr(self, ctx:LatteParser.EOrContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LatteParser#EInt.
    def visitEInt(self, ctx:LatteParser.EIntContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LatteParser#EUnOp.
    def visitEUnOp(self, ctx:LatteParser.EUnOpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LatteParser#EStr.
    def visitEStr(self, ctx:LatteParser.EStrContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LatteParser#EMulOp.
    def visitEMulOp(self, ctx:LatteParser.EMulOpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LatteParser#EAnd.
    def visitEAnd(self, ctx:LatteParser.EAndContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LatteParser#EParen.
    def visitEParen(self, ctx:LatteParser.EParenContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LatteParser#EFalse.
    def visitEFalse(self, ctx:LatteParser.EFalseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LatteParser#ENew.
    def visitENew(self, ctx:LatteParser.ENewContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LatteParser#EAddOp.
    def visitEAddOp(self, ctx:LatteParser.EAddOpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LatteParser#EAcc.
    def visitEAcc(self, ctx:LatteParser.EAccContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LatteParser#ENull.
    def visitENull(self, ctx:LatteParser.ENullContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LatteParser#EAccArr.
    def visitEAccArr(self, ctx:LatteParser.EAccArrContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LatteParser#addOp.
    def visitAddOp(self, ctx:LatteParser.AddOpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LatteParser#mulOp.
    def visitMulOp(self, ctx:LatteParser.MulOpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LatteParser#relOp.
    def visitRelOp(self, ctx:LatteParser.RelOpContext):
        return self.visitChildren(ctx)



del LatteParser
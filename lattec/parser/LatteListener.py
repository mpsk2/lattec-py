# Generated from lattec/parser/Latte.g4 by ANTLR 4.7.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .LatteParser import LatteParser
else:
    from LatteParser import LatteParser

# This class defines a complete listener for a parse tree produced by LatteParser.
class LatteListener(ParseTreeListener):

    # Enter a parse tree produced by LatteParser#program.
    def enterProgram(self, ctx:LatteParser.ProgramContext):
        pass

    # Exit a parse tree produced by LatteParser#program.
    def exitProgram(self, ctx:LatteParser.ProgramContext):
        pass


    # Enter a parse tree produced by LatteParser#FnDef.
    def enterFnDef(self, ctx:LatteParser.FnDefContext):
        pass

    # Exit a parse tree produced by LatteParser#FnDef.
    def exitFnDef(self, ctx:LatteParser.FnDefContext):
        pass


    # Enter a parse tree produced by LatteParser#ClsDef.
    def enterClsDef(self, ctx:LatteParser.ClsDefContext):
        pass

    # Exit a parse tree produced by LatteParser#ClsDef.
    def exitClsDef(self, ctx:LatteParser.ClsDefContext):
        pass


    # Enter a parse tree produced by LatteParser#argVec.
    def enterArgVec(self, ctx:LatteParser.ArgVecContext):
        pass

    # Exit a parse tree produced by LatteParser#argVec.
    def exitArgVec(self, ctx:LatteParser.ArgVecContext):
        pass


    # Enter a parse tree produced by LatteParser#arg.
    def enterArg(self, ctx:LatteParser.ArgContext):
        pass

    # Exit a parse tree produced by LatteParser#arg.
    def exitArg(self, ctx:LatteParser.ArgContext):
        pass


    # Enter a parse tree produced by LatteParser#block.
    def enterBlock(self, ctx:LatteParser.BlockContext):
        pass

    # Exit a parse tree produced by LatteParser#block.
    def exitBlock(self, ctx:LatteParser.BlockContext):
        pass


    # Enter a parse tree produced by LatteParser#Field.
    def enterField(self, ctx:LatteParser.FieldContext):
        pass

    # Exit a parse tree produced by LatteParser#Field.
    def exitField(self, ctx:LatteParser.FieldContext):
        pass


    # Enter a parse tree produced by LatteParser#Method.
    def enterMethod(self, ctx:LatteParser.MethodContext):
        pass

    # Exit a parse tree produced by LatteParser#Method.
    def exitMethod(self, ctx:LatteParser.MethodContext):
        pass


    # Enter a parse tree produced by LatteParser#Empty.
    def enterEmpty(self, ctx:LatteParser.EmptyContext):
        pass

    # Exit a parse tree produced by LatteParser#Empty.
    def exitEmpty(self, ctx:LatteParser.EmptyContext):
        pass


    # Enter a parse tree produced by LatteParser#BlockStmt.
    def enterBlockStmt(self, ctx:LatteParser.BlockStmtContext):
        pass

    # Exit a parse tree produced by LatteParser#BlockStmt.
    def exitBlockStmt(self, ctx:LatteParser.BlockStmtContext):
        pass


    # Enter a parse tree produced by LatteParser#Decl.
    def enterDecl(self, ctx:LatteParser.DeclContext):
        pass

    # Exit a parse tree produced by LatteParser#Decl.
    def exitDecl(self, ctx:LatteParser.DeclContext):
        pass


    # Enter a parse tree produced by LatteParser#Ass.
    def enterAss(self, ctx:LatteParser.AssContext):
        pass

    # Exit a parse tree produced by LatteParser#Ass.
    def exitAss(self, ctx:LatteParser.AssContext):
        pass


    # Enter a parse tree produced by LatteParser#Incr.
    def enterIncr(self, ctx:LatteParser.IncrContext):
        pass

    # Exit a parse tree produced by LatteParser#Incr.
    def exitIncr(self, ctx:LatteParser.IncrContext):
        pass


    # Enter a parse tree produced by LatteParser#Decr.
    def enterDecr(self, ctx:LatteParser.DecrContext):
        pass

    # Exit a parse tree produced by LatteParser#Decr.
    def exitDecr(self, ctx:LatteParser.DecrContext):
        pass


    # Enter a parse tree produced by LatteParser#Ret.
    def enterRet(self, ctx:LatteParser.RetContext):
        pass

    # Exit a parse tree produced by LatteParser#Ret.
    def exitRet(self, ctx:LatteParser.RetContext):
        pass


    # Enter a parse tree produced by LatteParser#VRet.
    def enterVRet(self, ctx:LatteParser.VRetContext):
        pass

    # Exit a parse tree produced by LatteParser#VRet.
    def exitVRet(self, ctx:LatteParser.VRetContext):
        pass


    # Enter a parse tree produced by LatteParser#Cond.
    def enterCond(self, ctx:LatteParser.CondContext):
        pass

    # Exit a parse tree produced by LatteParser#Cond.
    def exitCond(self, ctx:LatteParser.CondContext):
        pass


    # Enter a parse tree produced by LatteParser#CondElse.
    def enterCondElse(self, ctx:LatteParser.CondElseContext):
        pass

    # Exit a parse tree produced by LatteParser#CondElse.
    def exitCondElse(self, ctx:LatteParser.CondElseContext):
        pass


    # Enter a parse tree produced by LatteParser#While.
    def enterWhile(self, ctx:LatteParser.WhileContext):
        pass

    # Exit a parse tree produced by LatteParser#While.
    def exitWhile(self, ctx:LatteParser.WhileContext):
        pass


    # Enter a parse tree produced by LatteParser#ForEach.
    def enterForEach(self, ctx:LatteParser.ForEachContext):
        pass

    # Exit a parse tree produced by LatteParser#ForEach.
    def exitForEach(self, ctx:LatteParser.ForEachContext):
        pass


    # Enter a parse tree produced by LatteParser#SExp.
    def enterSExp(self, ctx:LatteParser.SExpContext):
        pass

    # Exit a parse tree produced by LatteParser#SExp.
    def exitSExp(self, ctx:LatteParser.SExpContext):
        pass


    # Enter a parse tree produced by LatteParser#TNonArray.
    def enterTNonArray(self, ctx:LatteParser.TNonArrayContext):
        pass

    # Exit a parse tree produced by LatteParser#TNonArray.
    def exitTNonArray(self, ctx:LatteParser.TNonArrayContext):
        pass


    # Enter a parse tree produced by LatteParser#TArray.
    def enterTArray(self, ctx:LatteParser.TArrayContext):
        pass

    # Exit a parse tree produced by LatteParser#TArray.
    def exitTArray(self, ctx:LatteParser.TArrayContext):
        pass


    # Enter a parse tree produced by LatteParser#TBasic.
    def enterTBasic(self, ctx:LatteParser.TBasicContext):
        pass

    # Exit a parse tree produced by LatteParser#TBasic.
    def exitTBasic(self, ctx:LatteParser.TBasicContext):
        pass


    # Enter a parse tree produced by LatteParser#TIdent.
    def enterTIdent(self, ctx:LatteParser.TIdentContext):
        pass

    # Exit a parse tree produced by LatteParser#TIdent.
    def exitTIdent(self, ctx:LatteParser.TIdentContext):
        pass


    # Enter a parse tree produced by LatteParser#TInt.
    def enterTInt(self, ctx:LatteParser.TIntContext):
        pass

    # Exit a parse tree produced by LatteParser#TInt.
    def exitTInt(self, ctx:LatteParser.TIntContext):
        pass


    # Enter a parse tree produced by LatteParser#TStr.
    def enterTStr(self, ctx:LatteParser.TStrContext):
        pass

    # Exit a parse tree produced by LatteParser#TStr.
    def exitTStr(self, ctx:LatteParser.TStrContext):
        pass


    # Enter a parse tree produced by LatteParser#TBool.
    def enterTBool(self, ctx:LatteParser.TBoolContext):
        pass

    # Exit a parse tree produced by LatteParser#TBool.
    def exitTBool(self, ctx:LatteParser.TBoolContext):
        pass


    # Enter a parse tree produced by LatteParser#TVoid.
    def enterTVoid(self, ctx:LatteParser.TVoidContext):
        pass

    # Exit a parse tree produced by LatteParser#TVoid.
    def exitTVoid(self, ctx:LatteParser.TVoidContext):
        pass


    # Enter a parse tree produced by LatteParser#NewObj.
    def enterNewObj(self, ctx:LatteParser.NewObjContext):
        pass

    # Exit a parse tree produced by LatteParser#NewObj.
    def exitNewObj(self, ctx:LatteParser.NewObjContext):
        pass


    # Enter a parse tree produced by LatteParser#NewObjArray.
    def enterNewObjArray(self, ctx:LatteParser.NewObjArrayContext):
        pass

    # Exit a parse tree produced by LatteParser#NewObjArray.
    def exitNewObjArray(self, ctx:LatteParser.NewObjArrayContext):
        pass


    # Enter a parse tree produced by LatteParser#NewBasicTypeArray.
    def enterNewBasicTypeArray(self, ctx:LatteParser.NewBasicTypeArrayContext):
        pass

    # Exit a parse tree produced by LatteParser#NewBasicTypeArray.
    def exitNewBasicTypeArray(self, ctx:LatteParser.NewBasicTypeArrayContext):
        pass


    # Enter a parse tree produced by LatteParser#item.
    def enterItem(self, ctx:LatteParser.ItemContext):
        pass

    # Exit a parse tree produced by LatteParser#item.
    def exitItem(self, ctx:LatteParser.ItemContext):
        pass


    # Enter a parse tree produced by LatteParser#EId.
    def enterEId(self, ctx:LatteParser.EIdContext):
        pass

    # Exit a parse tree produced by LatteParser#EId.
    def exitEId(self, ctx:LatteParser.EIdContext):
        pass


    # Enter a parse tree produced by LatteParser#EFunCall.
    def enterEFunCall(self, ctx:LatteParser.EFunCallContext):
        pass

    # Exit a parse tree produced by LatteParser#EFunCall.
    def exitEFunCall(self, ctx:LatteParser.EFunCallContext):
        pass


    # Enter a parse tree produced by LatteParser#ERelOp.
    def enterERelOp(self, ctx:LatteParser.ERelOpContext):
        pass

    # Exit a parse tree produced by LatteParser#ERelOp.
    def exitERelOp(self, ctx:LatteParser.ERelOpContext):
        pass


    # Enter a parse tree produced by LatteParser#ETrue.
    def enterETrue(self, ctx:LatteParser.ETrueContext):
        pass

    # Exit a parse tree produced by LatteParser#ETrue.
    def exitETrue(self, ctx:LatteParser.ETrueContext):
        pass


    # Enter a parse tree produced by LatteParser#ECast.
    def enterECast(self, ctx:LatteParser.ECastContext):
        pass

    # Exit a parse tree produced by LatteParser#ECast.
    def exitECast(self, ctx:LatteParser.ECastContext):
        pass


    # Enter a parse tree produced by LatteParser#EOr.
    def enterEOr(self, ctx:LatteParser.EOrContext):
        pass

    # Exit a parse tree produced by LatteParser#EOr.
    def exitEOr(self, ctx:LatteParser.EOrContext):
        pass


    # Enter a parse tree produced by LatteParser#EInt.
    def enterEInt(self, ctx:LatteParser.EIntContext):
        pass

    # Exit a parse tree produced by LatteParser#EInt.
    def exitEInt(self, ctx:LatteParser.EIntContext):
        pass


    # Enter a parse tree produced by LatteParser#EUnOp.
    def enterEUnOp(self, ctx:LatteParser.EUnOpContext):
        pass

    # Exit a parse tree produced by LatteParser#EUnOp.
    def exitEUnOp(self, ctx:LatteParser.EUnOpContext):
        pass


    # Enter a parse tree produced by LatteParser#EStr.
    def enterEStr(self, ctx:LatteParser.EStrContext):
        pass

    # Exit a parse tree produced by LatteParser#EStr.
    def exitEStr(self, ctx:LatteParser.EStrContext):
        pass


    # Enter a parse tree produced by LatteParser#EMulOp.
    def enterEMulOp(self, ctx:LatteParser.EMulOpContext):
        pass

    # Exit a parse tree produced by LatteParser#EMulOp.
    def exitEMulOp(self, ctx:LatteParser.EMulOpContext):
        pass


    # Enter a parse tree produced by LatteParser#EAnd.
    def enterEAnd(self, ctx:LatteParser.EAndContext):
        pass

    # Exit a parse tree produced by LatteParser#EAnd.
    def exitEAnd(self, ctx:LatteParser.EAndContext):
        pass


    # Enter a parse tree produced by LatteParser#EParen.
    def enterEParen(self, ctx:LatteParser.EParenContext):
        pass

    # Exit a parse tree produced by LatteParser#EParen.
    def exitEParen(self, ctx:LatteParser.EParenContext):
        pass


    # Enter a parse tree produced by LatteParser#EFalse.
    def enterEFalse(self, ctx:LatteParser.EFalseContext):
        pass

    # Exit a parse tree produced by LatteParser#EFalse.
    def exitEFalse(self, ctx:LatteParser.EFalseContext):
        pass


    # Enter a parse tree produced by LatteParser#ENew.
    def enterENew(self, ctx:LatteParser.ENewContext):
        pass

    # Exit a parse tree produced by LatteParser#ENew.
    def exitENew(self, ctx:LatteParser.ENewContext):
        pass


    # Enter a parse tree produced by LatteParser#EAcc.
    def enterEAcc(self, ctx:LatteParser.EAccContext):
        pass

    # Exit a parse tree produced by LatteParser#EAcc.
    def exitEAcc(self, ctx:LatteParser.EAccContext):
        pass


    # Enter a parse tree produced by LatteParser#EAddOp.
    def enterEAddOp(self, ctx:LatteParser.EAddOpContext):
        pass

    # Exit a parse tree produced by LatteParser#EAddOp.
    def exitEAddOp(self, ctx:LatteParser.EAddOpContext):
        pass


    # Enter a parse tree produced by LatteParser#ENull.
    def enterENull(self, ctx:LatteParser.ENullContext):
        pass

    # Exit a parse tree produced by LatteParser#ENull.
    def exitENull(self, ctx:LatteParser.ENullContext):
        pass


    # Enter a parse tree produced by LatteParser#EAccArr.
    def enterEAccArr(self, ctx:LatteParser.EAccArrContext):
        pass

    # Exit a parse tree produced by LatteParser#EAccArr.
    def exitEAccArr(self, ctx:LatteParser.EAccArrContext):
        pass


    # Enter a parse tree produced by LatteParser#addOp.
    def enterAddOp(self, ctx:LatteParser.AddOpContext):
        pass

    # Exit a parse tree produced by LatteParser#addOp.
    def exitAddOp(self, ctx:LatteParser.AddOpContext):
        pass


    # Enter a parse tree produced by LatteParser#mulOp.
    def enterMulOp(self, ctx:LatteParser.MulOpContext):
        pass

    # Exit a parse tree produced by LatteParser#mulOp.
    def exitMulOp(self, ctx:LatteParser.MulOpContext):
        pass


    # Enter a parse tree produced by LatteParser#relOp.
    def enterRelOp(self, ctx:LatteParser.RelOpContext):
        pass

    # Exit a parse tree produced by LatteParser#relOp.
    def exitRelOp(self, ctx:LatteParser.RelOpContext):
        pass



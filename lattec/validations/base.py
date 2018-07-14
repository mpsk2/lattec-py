import abc

from antlr4.Token import CommonToken
from antlr4.tree.Tree import TerminalNodeImpl

from lattec.parser import (
    Listener,
    Parser,
    Visitor,
)


class BaseState:
    def __init__(self):
        self.errors = []

    @staticmethod
    def normalize_name(name):
        if isinstance(name, str):
            return name
        elif isinstance(name, CommonToken):
            return name.text
        elif isinstance(name, TerminalNodeImpl):
            return name.getText()
        else:
            raise NotImplementedError(type(name))


class BaseListener(Listener, metaclass=abc.ABCMeta):
    @abc.abstractmethod
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


class BaseVisitor(Visitor):
    pass
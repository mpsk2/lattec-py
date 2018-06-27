from lattec.exceptions import LatteVariableNamesError
from lattec.parser.LatteListener import LatteListener
from lattec.parser.LatteParser import LatteParser
from lattec.validations.single_errors import Redeclaration, UndeclaredUse


class State:
    def __init__(self):
        self.names = {}
        self.redeclarations = []
        self.undeclared_uses = []

    def summarize(self):
        if self.redeclarations or self.undeclared_uses:
            raise LatteVariableNamesError(self.redeclarations, self.undeclared_uses)

    def add_name(self, name, line, level):
        if name in self.names:
            old_line, old_level = self.names[name]
            if old_level == level:
                self.redeclarations.append(Redeclaration(name, old_line, line))
                return

        self.names[name] = (line, level)

    def check_name(self, name, line):
        if name not in self.names:
            self.undeclared_uses.append(UndeclaredUse(name, line))


class LatteVariableUseListener(LatteListener):

    def enterProgram(self, ctx: LatteParser.ProgramContext):
        raise NotImplementedError()

    def enterFnDef(self, ctx: LatteParser.FnDefContext):
        raise NotImplementedError()

    def enterClsDef(self, ctx: LatteParser.ClsDefContext):
        raise NotImplementedError()

    def enterArgVec(self, ctx: LatteParser.ArgVecContext):
        raise NotImplementedError()

    def enterArg(self, ctx: LatteParser.ArgContext):
        raise NotImplementedError()

    def enterBlock(self, ctx: LatteParser.BlockContext):
        raise NotImplementedError()

    def enterField(self, ctx: LatteParser.FieldContext):
        raise NotImplementedError()

    def enterMethod(self, ctx: LatteParser.MethodContext):
        raise NotImplementedError()

    def enterEmpty(self, ctx: LatteParser.EmptyContext):
        raise NotImplementedError()

    def enterBlockStmt(self, ctx: LatteParser.BlockStmtContext):
        raise NotImplementedError()

    def enterDecl(self, ctx: LatteParser.DeclContext):
        raise NotImplementedError()

    def enterAss(self, ctx: LatteParser.AssContext):
        raise NotImplementedError()

    def enterIncr(self, ctx: LatteParser.IncrContext):
        raise NotImplementedError()

    def enterDecr(self, ctx: LatteParser.DecrContext):
        raise NotImplementedError()

    def enterRet(self, ctx: LatteParser.RetContext):
        raise NotImplementedError()

    def enterVRet(self, ctx: LatteParser.VRetContext):
        raise NotImplementedError()

    def enterCond(self, ctx: LatteParser.CondContext):
        raise NotImplementedError()

    def enterCondElse(self, ctx: LatteParser.CondElseContext):
        raise NotImplementedError()

    def enterWhile(self, ctx: LatteParser.WhileContext):
        raise NotImplementedError()

    def enterForEach(self, ctx: LatteParser.ForEachContext):
        raise NotImplementedError()

    def enterSExp(self, ctx: LatteParser.SExpContext):
        raise NotImplementedError()

    def enterArrAcc(self, ctx: LatteParser.ArrAccContext):
        raise NotImplementedError()

    def enterIdentVec(self, ctx: LatteParser.IdentVecContext):
        raise NotImplementedError()

    def enterTNonArray(self, ctx: LatteParser.TNonArrayContext):
        raise NotImplementedError()

    def enterTArray(self, ctx: LatteParser.TArrayContext):
        raise NotImplementedError()

    def enterTBasic(self, ctx: LatteParser.TBasicContext):
        raise NotImplementedError()

    def enterTIdent(self, ctx: LatteParser.TIdentContext):
        raise NotImplementedError()

    def enterTInt(self, ctx: LatteParser.TIntContext):
        raise NotImplementedError()

    def enterTStr(self, ctx: LatteParser.TStrContext):
        raise NotImplementedError()

    def enterTBool(self, ctx: LatteParser.TBoolContext):
        raise NotImplementedError()

    def enterTVoid(self, ctx: LatteParser.TVoidContext):
        raise NotImplementedError()

    def enterNew_expr_type(self, ctx: LatteParser.New_expr_typeContext):
        raise NotImplementedError()

    def enterItem(self, ctx: LatteParser.ItemContext):
        raise NotImplementedError()

    def enterEId(self, ctx: LatteParser.EIdContext):
        raise NotImplementedError()

    def enterEFunCall(self, ctx: LatteParser.EFunCallContext):
        raise NotImplementedError()

    def enterERelOp(self, ctx: LatteParser.ERelOpContext):
        raise NotImplementedError()

    def enterETrue(self, ctx: LatteParser.ETrueContext):
        raise NotImplementedError()

    def enterECast(self, ctx: LatteParser.ECastContext):
        raise NotImplementedError()

    def enterEOr(self, ctx: LatteParser.EOrContext):
        raise NotImplementedError()

    def enterEInt(self, ctx: LatteParser.EIntContext):
        raise NotImplementedError()

    def enterEUnOp(self, ctx: LatteParser.EUnOpContext):
        raise NotImplementedError()

    def enterEStr(self, ctx: LatteParser.EStrContext):
        raise NotImplementedError()

    def enterEMulOp(self, ctx: LatteParser.EMulOpContext):
        raise NotImplementedError()

    def enterEAnd(self, ctx: LatteParser.EAndContext):
        raise NotImplementedError()

    def enterEParen(self, ctx: LatteParser.EParenContext):
        raise NotImplementedError()

    def enterEFalse(self, ctx: LatteParser.EFalseContext):
        raise NotImplementedError()

    def enterENew(self, ctx: LatteParser.ENewContext):
        raise NotImplementedError()

    def enterEAddOp(self, ctx: LatteParser.EAddOpContext):
        raise NotImplementedError()

    def enterEAcc(self, ctx: LatteParser.EAccContext):
        raise NotImplementedError()

    def enterENull(self, ctx: LatteParser.ENullContext):
        raise NotImplementedError()

    def enterEAccArr(self, ctx: LatteParser.EAccArrContext):
        raise NotImplementedError()

    def enterAddOp(self, ctx: LatteParser.AddOpContext):
        raise NotImplementedError()

    def enterMulOp(self, ctx: LatteParser.MulOpContext):
        raise NotImplementedError()

    def enterRelOp(self, ctx: LatteParser.RelOpContext):
        raise NotImplementedError()

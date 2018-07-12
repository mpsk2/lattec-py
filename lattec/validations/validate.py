from lattec.parser.LatteParser import LatteParser
from lattec.validations.return_stmt import ReturnListener
from lattec.validations.var_use import VarUseListener


def validate(ctx: LatteParser.ProgramContext):
    listeners = [
        VarUseListener(),
        ReturnListener(),
    ]
    for listener in listeners:
        ctx.enterRule(listener)
        listener.summarize()
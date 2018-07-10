from lattec.parser.LatteParser import LatteParser
from lattec.validations.var_use import VarUseListener


def validate(ctx: LatteParser.ProgramContext):
    listeners = [
        VarUseListener(),
    ]
    for listener in listeners:
        ctx.enterRule(listener)
        listener.summarize()
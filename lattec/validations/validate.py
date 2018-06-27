from lattec.parser.LatteParser import LatteParser
from lattec.validations.variable_use import LatteVariableUseListener


def validate(ctx: LatteParser.ProgramContext):
    listeners = [
        LatteVariableUseListener()
    ]
    for listener in listeners:
        ctx.enterRule(listener)
        listener.summarize()
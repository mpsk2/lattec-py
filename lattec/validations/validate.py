from lattec.parser.LatteParser import LatteParser


def validate(ctx: LatteParser.ProgramContext):
    listeners = [
    ]
    for listener in listeners:
        ctx.enterRule(listener)
        listener.summarize()
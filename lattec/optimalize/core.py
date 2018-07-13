from functools import reduce

from lattec.optimalize.shorten_exprs import ShortenExprsVisitor
from lattec.parser import Parser


def optimize(ctx: Parser.ProgramContext):
    visitors = [
        ShortenExprsVisitor(),
    ]

    return reduce(
        lambda program, visitor: program.accept(visitor),
        visitors,
        ctx
    )
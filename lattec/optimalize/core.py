from functools import reduce

from lattec.optimalize.shorten_exprs import ShortenExprsVisitor
from lattec.parser import (
    Parser,
    parse_str,
)


def optimize(ctx: Parser.ProgramContext):
    visitors = [
        ShortenExprsVisitor(),
    ]

    return reduce(
        lambda program, visitor: parse_str(visitor.visit(program)).program(),
        visitors,
        ctx
    )
from antlr4 import (
    CommonTokenStream,
    FileStream,
)

from lattec.parser.LatteLexer import LatteLexer
from lattec.parser.LatteParser import LatteParser


def parse_file(path: str):
    content = FileStream(path)
    lexer = LatteLexer(content)
    stream = CommonTokenStream(lexer)
    parser = LatteParser(stream)
    return parser


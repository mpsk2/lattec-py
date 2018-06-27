from antlr4 import (
    CommonTokenStream,
    InputStream,
    FileStream,
)

from lattec.parser.LatteLexer import LatteLexer
from lattec.parser.LatteParser import LatteParser


def parse_content(content):
    lexer = LatteLexer(content)
    stream = CommonTokenStream(lexer)
    parser = LatteParser(stream)
    return parser


def parse_file(path: str):
    content = FileStream(path)
    return parse_content(content)


def parse_str(text: str):
    content = InputStream(text)
    return parse_content(content)


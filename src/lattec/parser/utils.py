from antlr4 import (
    CommonTokenStream,
    InputStream,
    FileStream,
)
from antlr4.error.ErrorListener import ErrorListener

from lattec.exceptions import LatteParserError, LatteSyntaxError
from lattec.parser.LatteLexer import LatteLexer
from lattec.parser.LatteParser import LatteParser


class LatteParseErrorListener(ErrorListener):
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        raise LatteSyntaxError(offendingSymbol, line, column, msg) from e

    def reportAmbiguity(self, recognizer, dfa, startIndex, stopIndex, exact, ambigAlts, configs):
        raise LatteParserError()

    def reportAttemptingFullContext(self, recognizer, dfa, startIndex, stopIndex, conflictingAlts, configs):
        raise LatteParserError()

    def reportContextSensitivity(self, recognizer, dfa, startIndex, stopIndex, prediction, configs):
        raise LatteParserError()


def parse_content(content):
    lexer = LatteLexer(content)
    lexer.removeErrorListeners()
    lexer.addErrorListener(LatteParseErrorListener())

    stream = CommonTokenStream(lexer)

    parser = LatteParser(stream)
    parser.removeErrorListeners()
    parser.addErrorListener(LatteParseErrorListener())

    return parser


def parse_file(path: str):
    content = FileStream(path)
    return parse_content(content)


def parse_str(text: str):
    content = InputStream(text)
    return parse_content(content)


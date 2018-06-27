import typing

from lattec.validations.single_errors import Redeclaration, UndeclaredUse


class LatteException(Exception):
    pass


class LatteError(LatteException):
    pass


class LatteParserError(LatteError):
    pass


class LatteSyntaxError(LatteParserError):
    def __init__(self, offending_symbol, line, column, message, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.offending_symbol = offending_symbol
        self.line = line
        self.column = column
        self.message = message

    def __repr__(self):
        return 'Syntax error at line:column={}:{}\n{}'.format(
            self.line,
            self.column,
            repr(self.message),
        )

    def __str__(self):
        return 'Syntax error at line:column={}:{}\n{}'.format(
            self.line,
            self.column,
            self.message,
        )


class LatteValidationError(LatteError):
    pass


class LatteVariableNamesError(LatteError):
    def __init__(self, redeclarations: typing.List[Redeclaration], undeclared_uses: typing.List[UndeclaredUse], *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.redeclarations = redeclarations
        self.undeclared_uses = undeclared_uses

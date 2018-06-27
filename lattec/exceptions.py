class LatteException(Exception):
    pass


class LatteError(LatteException):
    pass


class LatteParserError(LatteError):
    pass


class LatteSyntaxError(LatteParserError):
    def __init__(self, offending_symbol, line, column, message, *args, **kwargs):
        super().__init__(message, *args, **kwargs)
        self.offending_symbol = offending_symbol
        self.line = line
        self.column = column

    def __repr__(self):
        return super().__repr__() + '{}, {}, {}, {}'.format(
            repr(self.offending_symbol),
            repr(self.line),
            repr(self.column),
            repr(self.message),
        )

    def __str__(self):
        return super().__str__() + '{}, {}, {}, {}'.format(
            str(self.offending_symbol),
            self.line,
            self.column,
            self.message,
        )
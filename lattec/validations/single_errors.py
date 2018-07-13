from collections import namedtuple


class Redeclaration(namedtuple('redeclaration', ['name', 'old_line', 'new_line'])):
    def __str__(self):
        return 'variable {} has been declared at line {}, but has been earlier declared at line {}'.format(
            self.name,
            self.old_line,
            self.new_line
        )


class UndeclaredUse(namedtuple('undeclared_use', ['name', 'line'])):
    def __str__(self):
        return 'variable {} has been used at line {}, but has not been declared earlier'.format(
            self.name,
            self.line
        )


class TypeMissMatch(namedtuple('type_miss_match', ['t1', 't2', 'line'])):
    def ___str___(self):
        return 'got {}, expected {} at line {}'.format(
            self.t1,
            self.t2,
            self.line,
        )


class AdditionalArgument(namedtuple('additional_argument', ['func_name', 'arg', 'line'])):
    def __str__(self):
        return 'function {} has been passed with additional argument {} at line {}'.format(
            self.func_name,
            self.name,
            self.line
        )


class MissingArgument(namedtuple('missing_argument', ['func_name', 'name', 'line'])):
    def __str__(self):
        return 'function {} misses argument {} at line {}'.format(
            self.func_name,
            self.name,
            self.line
        )


class NoReturn(namedtuple('no_return', ['name', 'line'])):
    def __str__(self):
        return 'no return at non void function {} starting at line {}'.format(
            self.name,
            self.line,
        )
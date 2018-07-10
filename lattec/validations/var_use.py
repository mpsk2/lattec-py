from copy import deepcopy

from lattec.validations.base import (
    BaseListener,
    BaseVisitor,
)
from lattec.validations.single_errors import (
    Redeclaration,
    UndeclaredUse,
)


class State:
    def __init__(self):
        self.level = 0
        self.vars = {}
        self.errors = []
        self.vars_stack = []

    def add_var(self, name, type_, new_line):
        if name in self.vars:
            level, old_line, _ = self.vars[name]
            if level == self.level:
                self.errors.append(Redeclaration(name, old_line, new_line))

        self.vars[name] = (self.level, new_line, type_)

    def use_var(self, name, line):
        if name not in self.vars:
            self.errors.append(UndeclaredUse(name, line))
            return

        _, _, type_ = self.vars[name]

        return type_

    def level_up(self):
        self.level += 1
        self.vars_stack.append(deepcopy(self.vars))

    def level_down(self):
        self.level -= 1
        assert self.level >= 0
        self.vars = self.vars_stack[-1]
        self.vars_stack.pop()


class VarUseVisitor(BaseVisitor):
    def __init__(self, state):
        self.state = state


class VarUseListener(BaseListener):
    def __init__(self):
        self.state = State()
        self.visitor = VarUseVisitor(self.state)
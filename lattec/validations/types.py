import abc
from typing import (
    List,
    Dict,
)


class LatteType(metaclass=abc.ABCMeta):
    @property
    @abc.abstractmethod
    def methods(self):
        pass

    @abc.abstractmethod
    def __eq__(self, other):
        pass

    @abc.abstractmethod
    def __repr__(self):
        pass


class LatteBasicType(LatteType, metaclass=abc.ABCMeta):
    @property
    def methods(self):
        return {}

    def __eq__(self, other):
        return isinstance(other, self.__class__)

    def __repr__(self):
        return self.__class__.__name__.replace('Latte', '')


class LatteVoid(LatteBasicType):
    pass


class LatteInt(LatteBasicType):
    pass


class LatteBool(LatteBasicType):
    pass


class LatteString(LatteBasicType):
    pass


class LatteArray(LatteType):
    def __init__(self, t: LatteType):
        self.t = t

    @property
    def methods(self):
        return {
            'length': LatteInt(),
        }

    def __eq__(self, other):
        return isinstance(other, LatteArray) and (self.t == other.t)

    def __repr__(self):
        return 'Array({})'.format(repr(self.t))


class LatteFunction(LatteType):
    def __init__(self, args: List[LatteType], ret: LatteType):
        self.args = args
        self.ret = ret

    @property
    def methods(self):
        return {
            '__call__': self.ret
        }

    def __eq__(self, other):
        return isinstance(other, LatteFunction) and (self.args == other.args) and (self.ret == other.ret)

    def __repr__(self):
        return 'Function(({}) => {})'.format(
            ','.join(map(repr, self.args)),
            repr(self.ret),
        )


class LatteClass(LatteType):
    def __init__(self, name: str, fields: Dict[str, LatteType]):
        self.name = name
        self.fields = fields

    @property
    def methods(self):
        return {}

    def __eq__(self, other):
        return isinstance(other, LatteClass) and (self.name == other.name)

    def __repr__(self):
        return self.name


class LatteNull(LatteType):
    @property
    def methods(self):
        return {}

    def __eq__(self, other):
        return isinstance(other, LatteObject)

    def __repr__(self):
        return 'Null'


class LatteObject(LatteType):
    def __init__(self, c: LatteClass):
        self.c = c

    @property
    def methods(self):
        return self.c.fields

    def __eq__(self, other):
        return isinstance(other, LatteNull) or (isinstance(other, LatteObject) and (self.c == other.c))

    def __repr__(self):
        return 'Obj of {}'.format(self.c.name)


INITIAL_FEED = {
    'printInt': LatteFunction([LatteInt()], LatteVoid()),
    'printString': LatteFunction([LatteString()], LatteVoid()),
    'readInt': LatteFunction([], LatteInt()),
    'readString': LatteFunction([], LatteString()),
}

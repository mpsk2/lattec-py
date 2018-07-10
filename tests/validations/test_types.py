import pytest

from lattec.validations.types import *

TYPES = (
    (LatteBool(), {}),
    (LatteInt(), {}),
    (LatteVoid(), {}),
    (LatteString(), {}),
    (LatteArray(LatteBool()), {'length': LatteInt()}),
    (LatteArray(LatteInt()), {'length': LatteInt()}),
    (LatteFunction([], LatteVoid()), {'__call__': LatteVoid()}),
    (
        LatteClass(
            'abc',
            {'a': LatteInt(), 'b': LatteFunction([], LatteInt())}
        ),
        {'a': LatteInt(), 'b': LatteFunction([], LatteInt())},
    ),
)

TEST_CASES_TYPES_EQ = (
    (TYPES[i][0], TYPES[j][0], i == j)
    for i in range(len(TYPES))
    for j in range(len(TYPES))
)


@pytest.mark.parametrize('t1,t2,eq', TEST_CASES_TYPES_EQ)
def test_eq(t1: LatteType, t2: LatteType, eq: bool):
    assert (t1 == t2) == eq


@pytest.mark.parametrize('t, methods', TYPES)
def test_methods(t: LatteType, methods):
    assert t.methods == methods

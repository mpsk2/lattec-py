import pytest

from lattec.parser import parse_str
from lattec.validations.var_use import VarUseListener

PROGRAMS = (
    'void main() { }',
    'void main(int a, int b, int c) { return; }'
)


@pytest.mark.parametrize('code', PROGRAMS)
def test_var_use(code):
    parser = parse_str(code)
    program = parser.program()
    listener = VarUseListener()
    program.enterRule(listener)

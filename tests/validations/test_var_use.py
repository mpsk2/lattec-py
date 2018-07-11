import pytest

from lattec.parser import parse_str
from lattec.validations.var_use import VarUseListener

PROGRAMS = (
    'void main() { }',
    'void main(int a, int b, int c) { return; }',
    'int a() { return 1; }',
    'boolean b() { return true; }',
    'boolean b() { return false; }',
    '''
    void a() {
        int b, c, d;
        int e = 4;
    }
    ''',
    '''
    void b() {
        boolean a;
        if (a) {
            return;
        }
    }
    ''',
    '''
    void b() {
        boolean a;
        if (a) {
            return;
        } else {
            return;
        }
    }
    ''',
    '''
    void b() {
        boolean a;
        while (a) {
            return;
        }
    }
    ''',
)


@pytest.mark.parametrize('code', PROGRAMS)
def test_var_use(code):
    parser = parse_str(code)
    program = parser.program()
    listener = VarUseListener()
    program.enterRule(listener)

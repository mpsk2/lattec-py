import glob

import pytest

from lattec.parser import (
    parse_file,
    parse_str,
)
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
    '''
    void a() {
        int f, b, c, d;
        f = 1;
        b = 2;
        c = 3;
        d = b + c * f;
    }
    ''',
)


@pytest.mark.parametrize('code', PROGRAMS)
def test_var_use(code):
    parser = parse_str(code)
    program = parser.program()
    listener = VarUseListener()
    program.enterRule(listener)


@pytest.mark.parametrize("file_path", glob.iglob('tests/parser/good/core/*.lat', recursive=True))
def test_good_core_files(file_path):
    parser = parse_file(file_path)
    propgram = parser.program()
    listener = VarUseListener()
    propgram.enterRule(listener)
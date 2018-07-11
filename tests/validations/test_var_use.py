import glob

import pytest

from lattec.exceptions import LatteVariableNamesError
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
    '''
    void declArray() {
        int[] a;
    }
    ''',
    '''
    void initArray() {
        int[] a = new int[10];
    }
    ''',
    # '''
    # void accessArrayLength() {
    #     int[] a = new init[10];
    #     int b = a.length;
    # }
    # ''',
    '''
    void assignArrayValue() {
        int[] a = new int[10];
        a[5] = 1;
    }
    ''',
    '''
    void acceessArrayFieldValue() {
        int[] a = new int[10];
        int b = a[1] + a[3] + 5;
    }
    ''',
)

FAILING_TESTS = (
    (
        'returns int for void',
        '''
        void a() {
            return 1;
        }
        '''
    ),
)


@pytest.mark.parametrize('code', PROGRAMS)
def test_var_use(code):
    parser = parse_str(code)
    program = parser.program()
    listener = VarUseListener()
    program.enterRule(listener)
    listener.summarize()


@pytest.mark.parametrize("file_path", glob.iglob(r'tests/parser/good/core/*.lat', recursive=True))
def test_good_core_files(file_path):
    parser = parse_file(file_path)
    propgram = parser.program()
    listener = VarUseListener()
    propgram.enterRule(listener)
    listener.summarize()\


@pytest.mark.parametrize("file_path", glob.iglob(r'tests/parser/good/extensions/**/*.lat', recursive=True))
def test_good_extensions_files(file_path):
    parser = parse_file(file_path)
    propgram = parser.program()
    listener = VarUseListener()
    propgram.enterRule(listener)
    listener.summarize()


@pytest.mark.parametrize('name, code', FAILING_TESTS)
def test_var_use_failing(name, code):
    parser = parse_str(code)
    program = parser.program()
    listener = VarUseListener()
    program.enterRule(listener)
    with pytest.raises(LatteVariableNamesError):
        listener.summarize()
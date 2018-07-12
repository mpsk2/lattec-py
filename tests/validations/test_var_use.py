import glob

import pytest

from lattec.exceptions import LatteVariableNamesError
from lattec.parser import (
    parse_file,
    parse_str,
)
from lattec.validations.var_use import VarUseListener

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


@pytest.mark.parametrize("file_path", glob.iglob(r'tests/parser/good/core/*.lat', recursive=True))
def test_good_core_files(file_path):
    parser = parse_file(file_path)
    propgram = parser.program()
    listener = VarUseListener()
    propgram.enterRule(listener)
    listener.summarize()


@pytest.mark.parametrize(
    "file_path",
    [
        file_path
        for file_path in glob.iglob(r'tests/parser/good/extensions/**/*.lat', recursive=True)
        if 'part' not in file_path
    ]
)
def test_good_extensions_files(file_path):
    parser = parse_file(file_path)
    propgram = parser.program()
    listener = VarUseListener()
    propgram.enterRule(listener)
    listener.summarize()


@pytest.mark.parametrize("file_path", glob.iglob(r'tests/parser/good/self/*.lat', recursive=True))
def test_good_self_files(file_path):
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
import glob

import pytest

from lattec.exceptions import LatteReturnError
from lattec.parser import parse_file
from lattec.validations.return_stmt import ReturnListener


@pytest.mark.parametrize("file_path", glob.iglob(r'tests/parser/good/core/*.lat', recursive=True))
def test_good_core_files(file_path):
    parser = parse_file(file_path)
    propgram = parser.program()
    listener = ReturnListener()
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
    listener = ReturnListener()
    propgram.enterRule(listener)
    listener.summarize()


@pytest.mark.parametrize("file_path", glob.iglob(r'tests/parser/good/self/*.lat', recursive=True))
def test_good_self_files(file_path):
    parser = parse_file(file_path)
    propgram = parser.program()
    listener = ReturnListener()
    propgram.enterRule(listener)
    listener.summarize()


@pytest.mark.parametrize("file_path", glob.iglob(r'tests/parser/bad/no_return/*.lat', recursive=True))
def test_var_use_failing(file_path):
    parser = parse_file(file_path)
    program = parser.program()
    listener = ReturnListener()
    program.enterRule(listener)
    with pytest.raises(LatteReturnError):
        listener.summarize()


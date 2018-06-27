import glob

import pytest

from lattec.exceptions import LatteSyntaxError
from lattec.parser import parse_str, parse_file


def test_empty():
    empty = 'int main() { }'
    parser = parse_str(empty)
    parser.program()


def test_empty_no_finish():
    empty = 'int main() {'
    parser = parse_str(empty)
    with pytest.raises(LatteSyntaxError):
        parser.program()


@pytest.mark.parametrize("file_path", glob.iglob('tests/parser/**/*.lat', recursive=True))
def test_file(file_path):
    parser = parse_file(file_path)
    if 'syntax' in file_path:
        with pytest.raises(LatteSyntaxError):
            parser.program()
    else:
        parser.program()
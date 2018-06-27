import pytest

from lattec.parser import parse_str


def test_empty():
    empty = 'int main() { }'
    parser = parse_str(empty)
    parser.program()

def test_empty_no_finish():
    empty = 'int main() {'
    parser = parse_str(empty)
    with pytest.raises(Exception):
        parser.program()

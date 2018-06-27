import glob
import sys

import pytest

from lattec.core import main_f


@pytest.mark.parametrize("file_path", glob.iglob('tests/parser/bad/**/*.lat', recursive=True))
def test_bad_file(monkeypatch, file_path):
    monkeypatch.setattr(sys, 'argv', ['prog', file_path])

    with pytest.raises(Exception):
        main_f()
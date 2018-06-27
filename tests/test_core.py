import glob
import sys

import pytest

from lattec.core import main_f


@pytest.mark.parametrize("file_path", glob.iglob('tests/parser/bad/**/*.lat', recursive=True))
def test_bad_file(monkeypatch, file_path):
    monkeypatch.setattr(sys, 'argv', ['prog', file_path])

    with pytest.raises(Exception) as cm:
        main_f()

    assert cm.type != NotImplementedError


@pytest.mark.parametrize("file_path", glob.iglob('tests/parser/good/**/*.lat', recursive=True))
def test_good_file_pass_validation(monkeypatch, file_path):
    monkeypatch.setattr(sys, 'argv', ['prog', file_path, '--validation-only'])

    main_f()

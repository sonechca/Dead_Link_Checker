import pytest
import DLFunctions as dlf


def test_check_no_file():
    with pytest.raises(FileNotFoundError):
        dlf.file_chekcer("", "a")
import pytest

from .timedata import Timedata


@pytest.parametrize("input_string, expected_result", ["2:30:30", Timedata(2, 30, 30)])
def test_from_string(input_string, expected_result):
    assert Timedata.from_string(input_string) == expected_result

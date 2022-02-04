import pytest

from timedata import Timedata


def test_eq_comparsion():
    assert Timedata(2, 10, 0) == Timedata(2, 10, 0)


def test_lt_comparsion():
    assert Timedata(2, 10, 0) < Timedata(2, 10, 1)
    assert Timedata(2, 10, 0) < Timedata(2, 11, 0)
    assert Timedata(2, 10, 0) < Timedata(3, 10, 0)


def test_gt_comparsion():
    assert Timedata(2, 10, 1) > Timedata(2, 10, 0)
    assert Timedata(2, 11, 0) > Timedata(2, 10, 0)
    assert Timedata(3, 10, 0) > Timedata(2, 10, 0)


@pytest.mark.parametrize(
    "input_string, expected_result",
    [
        ["2:30:30", Timedata(2, 30, 30)],
        ["2:00:00", Timedata(2, 0, 0)],
        ["200:01:01", Timedata(200, 1, 1)],
    ],
)
def test_from_string(input_string, expected_result):
    result = Timedata.from_string(input_string)
    assert result == expected_result


@pytest.mark.parametrize(
    "expected_result, input",
    [
        ["2:30:30", Timedata(2, 30, 30)],
        ["2:00:00", Timedata(2, 0, 0)],
        ["200:01:01", Timedata(200, 1, 1)],
    ],
)
def test_to_string(expected_result, input):
    result = input.to_string()
    assert result == expected_result

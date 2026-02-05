import pytest
from python_foundations.basics.clamp import clamp


def test_clamp_inside_interval():
    assert clamp(5, 0, 10) == 5


def test_clamp_below_interval():
    assert clamp(-3, 0, 10) == 0


def test_clamp_above_interval():
    assert clamp(15, 0, 10) == 10


def test_clamp_invalid_interval():
    with pytest.raises(ValueError):
        clamp(5, 10, 0)

"""Value checks test."""
from value_check import int_positive_check, float_check, date_check


def test_int_positive_check():
    """Test function int_positive_check()."""
    assert int_positive_check('5') is True
    assert int_positive_check('0') is False
    assert int_positive_check('3.14') is False
    assert int_positive_check('-5') is False
    assert int_positive_check('s') is False


def test_float_check():
    """Test function float_check()."""
    assert float_check('5.0') is True
    assert float_check('0.0') is True
    assert float_check('-5.0') is True
    assert float_check('s') is False


def test_data_check():
    """Test function date_check()."""
    assert date_check('01-01-2024') is True
    assert date_check('01-01-24') is False
    assert date_check('2024-01-01') is False
    assert date_check('5') is False
    assert date_check('s') is False

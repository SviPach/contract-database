"""Main test."""
import main


def test_main_int_positive_check():
    """Test function int_positive_check() in main()."""
    assert main.value_check.int_positive_check("1") is True

    assert main.value_check.int_positive_check("0") is False
    assert main.value_check.int_positive_check("-1") is False
    assert main.value_check.int_positive_check("one") is False

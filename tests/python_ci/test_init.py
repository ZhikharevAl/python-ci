"""Unit tests for the `python_ci` module."""

from src.python_ci.main import generate_list


def test_generate_list() -> None:
    """Test that `generate_list` returns the expected value."""
    assert generate_list() == 42

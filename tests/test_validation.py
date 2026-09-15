import pytest

from validation import validate_k


def test_valid_k():

    assert validate_k(3) is True


def test_invalid_k():

    with pytest.raises(ValueError):

        validate_k(1)


def test_too_large_k():

    with pytest.raises(ValueError):

        validate_k(25)

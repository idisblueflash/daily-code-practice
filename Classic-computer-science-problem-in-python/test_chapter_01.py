import pytest

from chapter_01 import fib1, fib2, fib25


def test_fibonacci_infinite_loop():
    with pytest.raises(RecursionError):
        fib1(5)


def test_fibonacci_without_exception():
    fib2(5)


def test_fibonacci_exponentially():
    assert fib25(10, counter=0) == 55



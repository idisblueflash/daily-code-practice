import pytest


def fib1(n: int) -> int:
    return fib1(n-1) + fib1(n-2)


def test_fibonacci_infinite_loop():
    with pytest.raises(RecursionError):
        fib1(5)


def fib2(n: int) -> int:
    if n < 2:
        return n
    return fib2(n - 1) + fib2(n - 2)


def test_fibonacci_without_exception():
    fib2(5)



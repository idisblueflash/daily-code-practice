def fib1(n: int) -> int:
    return fib1(n-1) + fib1(n-2)


def fib2(n: int) -> int:
    if n < 2:
        return n
    return fib2(n - 1) + fib2(n - 2)


def fib25(n: int, counter: int) -> int:
    if n < 2:
        return counter
    counter += 1
    return fib2(n - 1) + fib2(n - 2)

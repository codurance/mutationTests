from typing import Literal


def add(summand_1: int, summand_2: int) -> int:
    return summand_1 + summand_2


def subtract(minuend: int, subtrahend: int) -> int:
    return minuend - subtrahend


def multiply(factor_1: int, factor_2: int) -> int:
    return factor_1 * factor_2


def divide(dividend: int, divisor: int) -> int:
    return int(dividend / divisor)


def summation(start: int) -> int:
    value = 0
    while start > 0:
        value += start
        start -= 1
    return value


def is_positive(number: int) -> bool:
    return number > 0


def compare(number_1: int, number_2: int) -> Literal[-1, 0, 1]:
    if number_1 == number_2:
        value: Literal[0] = 0
    elif number_1 > number_2:
        value: Literal[1] = 1  # type: ignore[no-redef]
    else:
        value: Literal[-1] = -1  # type: ignore[no-redef]

    return value

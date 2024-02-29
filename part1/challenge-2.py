#!/usr/bin/env python


def input_pow():
    """
    pow input number
    :return: int pow input
    """
    try:
        x = input("type a number:")
        x = int(x)
        return x**2
    except ValueError:
        print("Not a number")


print(input_pow())


def my_print(s: str):
    """
    print params
    :param s: str.
    :return: None
    """
    print(s)


my_print("myprint")


def three_recomend_two_option(a: int, b: int, c: int, x: int=4, y: int=5):
    """
    return all sum
    :param a: int.
    :param b: int.
    :param c: int.
    :param x (optional): int (default 4).
    :param y (optional): int (default 5)
    :return: int sum all param
    """
    return a + b + c + x + y


print(three_recomend_two_option(1, 2, 3))


def to_float():
    """
    convert input number to float.
    :return: float.
    """
    s = input("type a number")
    try:
        s = float(s)
        return s
    except ValueError:
        print("Not a number")


print(to_float())

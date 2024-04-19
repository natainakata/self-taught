import math


def isPalindrome(x: int):
    if x < 0:
        return False
    elif x == 0:
        return True
    else:
        d = digit(x)
        return validate(x, d)


def validate(x: int, d: int):
    if d > 0:
        start = round_start(x)
        end = round_end(x)
        if start == end:
            if d == 2:
                return True
            start = start * (10**d)
            next_num = x - (start + end)
            if next_num == 0:
                return True
            else:
                next_num /= 10
                return validate(int(next_num), digit(next_num))
        else:
            return False
    if digit == 0:
        return True


def digit(x: int) -> int:
    return int(math.log10(x))


def round_start(x: int) -> int:
    digit = int(math.log10(x))
    return round(x, -digit) // 10**digit


def round_end(x: int) -> int:
    if x == 0:
        return x
    digit = int(math.log10(x))
    if digit > 0:
        start = round(x, -digit)
        return round_end(x - start)
    else:
        return x

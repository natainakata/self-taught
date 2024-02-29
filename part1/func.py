def f(x):
    return x * 2


result = f(2)
print(result)


def f2(x):
    return x + 1


z = f(4)

if z == 5:
    print("z is 5")
else:
    print("z is not 5")


def f3():
    return 1 + 1


result = f3()
print(result)


def f4(x, y, z):
    return x + y + z


result = f4(1, 2, 3)
print(result)


def even_odd(x):
    if x % 2 == 0:
        print("偶数")
    else:
        print("奇数")


even_odd(2)
even_odd(3)


def f5(x=2):
    return x ** x


print(f5())
print(f5(6))

def add_it(x, y=10):
    return x + y


result = add_it(2)
print(result)

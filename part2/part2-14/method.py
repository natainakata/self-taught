class Lion:
    def __init__(self, name) -> None:
        self.name = name

    def __repr__(self) -> str:
        return self.name


lion = Lion("Dilbert")
print(lion)


class AlwaysPositive:
    def __init__(self, number) -> None:
        self.n = number

    def __add__(self, other):
        return abs(self.n + other.n)


x = AlwaysPositive(-20)
y = AlwaysPositive(10)
print(x + y)

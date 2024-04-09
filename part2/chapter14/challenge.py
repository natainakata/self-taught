class Square:
    square_list = []

    def __init__(self, w) -> None:
        self.width = w
        self.square_list.append(self)

    def __repr__(self) -> str:
        return f"{self.width} by {self.width} by {self.width} by {self.width}"


def compare(a, b) -> bool:
    return a is b


square1 = Square(10)
square2 = Square(16)
print(square1)
print(square2)
print(Square.square_list)
print(compare(square1, square1))
print(compare(square1, square2))

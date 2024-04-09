class Shape:
    def __init__(self) -> None:
        pass

    def what_am_i(self) -> str:
        return "I am shape"


class Rectangle(Shape):
    def __init__(self, w: int, h: int) -> None:
        self.width = w
        self.height = h

    def calcurate_perimeter(self):
        return self.width * 2 + self.height * 2


class Square(Shape):
    def __init__(self, w: int) -> None:
        self.width = w

    def change_size(self, w: int):
        self.width += w

    def calcurate_perimeter(self):
        return self.width * 4


class Horse:
    def __init__(self, name, rider) -> None:
        self.name = name
        self.rider = rider


class Rider:
    def __init__(self, name) -> None:
        self.name = name


rectangle = Rectangle(10, 20)
square = Square(20)
print(rectangle.calcurate_perimeter())
print(square.calcurate_perimeter())
square.change_size(3)
print(square.calcurate_perimeter())
square.change_size(-6)
print(square.calcurate_perimeter())
print(rectangle.what_am_i())
print(square.what_am_i())
rider = Rider("Raida")
horse = Horse("UMA", rider)
print(horse.rider.name)

class Rectangle:
    recs = []

    def __init__(self, w, l) -> None:
        self.width = w
        self.len = l
        self.recs.append((self.width, self.len))

    def print_size(self):
        print("{} by {}".format(self.width, self.len))


r1 = Rectangle(10, 24)
r1.print_size()
r2 = Rectangle(20, 40)
r3 = Rectangle(100, 200)
print(Rectangle.recs)

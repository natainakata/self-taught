class Dog:
    def __init__(self, name, breed, owner) -> None:
        self.name = name
        self.breed = breed
        self.owner = owner


class Person:
    def __init__(self, name) -> None:
        self.name = name


mick = Person("Mick Jagger")
stan = Dog("Stanley", "Bulldog", mick)
print(stan.owner.name)

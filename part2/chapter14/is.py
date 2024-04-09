class Person:
    def __init__(self) -> None:
        self.name = "Bob"


bob = Person()
same_bob = bob
print(bob is same_bob)

another_bob = Person()
print(bob is another_bob)

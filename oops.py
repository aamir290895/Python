class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def do(self):
        print(f"g name is {self.name} and breed is {self.breed} years old.")

d = Dog("german sufford", "indian")

d.do()
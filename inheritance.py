# Define a base class (superclass) called 'Animal'
class Animal:
    def __init__(self, name):
        self.name = name

    def make_sound(self):
        pass  # Placeholder for the sound method

# Define a derived class (subclass) called 'Dog' that inherits from 'Animal'
class Dog(Animal):
    def make_sound(self):
        return "Woof!"

# Define another derived class (subclass) called 'Cat' that also inherits from 'Animal'
class Cat(Animal):
    def make_sound(self):
        return "Meow!"

# Create instances of the derived classes
dog_instance = Dog(name="Buddy")
cat_instance = Cat(name="Whiskers")

# Accessing attributes and calling methods
print(f"{dog_instance.name} says: {dog_instance.make_sound()}")
# Output: Buddy says: Woof!

print(f"{cat_instance.name} says: {cat_instance.make_sound()}")
# Output: Whiskers says: Meow!

class Dog:

    species = "Dog"

    def __init__(self, name, age):
        self.name = name
        self.age = age

wolfie = Dog("Wolfie", 5)
max = Dog("Max", 8)

print("Wolfie is a {}".format(wolfie.species))
print("Max is a {}".format(max.species))

print("{} is {} years old".format(wolfie.name, wolfie.age))
print("{} is {} years old".format(max.name, max.age))
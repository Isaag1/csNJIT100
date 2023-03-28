"""
Isaac Guerrero
CS 100 Section 015
HW08,November 7, 2021
"""

# 1


class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed


lexi = Dog('lexi', 'shih-tzu')
print(lexi.name)
print(lexi.breed)

# 2


class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed
        self.tricks = []


lexi = Dog('lexi', 'shih-tzu')
print(lexi.name)
print(lexi.breed)
print(lexi.tricks)


# 3
class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed
        self.tricks = []

    def teach(self, trick):
        self.tricks.append(trick)
        print(f"{self.name} knows {trick}")


lexi = Dog('lexi', 'shih-tzu')
print(lexi.name)
print(lexi.breed)
lexi.teach('frisbe')
print(lexi.teach)

# 4


class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed
        self.tricks = []

    def teach(self, trick):
        self.tricks.append(trick)
        print(f"{self.name} knows {trick}")

    def knows(self, trick):
        if trick in self.tricks:
            print(f"Yes, {self.name} knows {trick}")
            return True
        else:
            print(f"No, {self.name} doesn't know {trick}")
            return False


lexi = Dog('lexi', 'shih-tzu')
print(lexi.name)
print(lexi.breed)
lexi.teach('frisbe')
print(lexi.teach)
lexi.knows("FETCH")
print(lexi.knows)


# 5
class Dog:
    species = 'Canis familiaris'

    def __init__(self, name, breed):
        self.name = name
        self.breed = breed
        self.tricks = []

    def teach(self, trick):
        self.tricks.append(trick)
        print(f"{self.name} knows {trick}")

    def knows(self, trick):
        if trick in self.tricks:
            print(f"Yes, {self.name} knows {trick}")
            return True
        else:
            print(f"No, {self.name} doesn't know {trick}")
            return False


lexi = Dog('lexi', 'shih-tzu')
print(lexi.name)
print(lexi.breed)
lexi.teach('frisbe')
print(lexi.teach)
lexi.knows("frisbe")
print(lexi.knows)
print(lexi.species)

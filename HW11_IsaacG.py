"""
Isaac Guerrero
CS 100 Section 015
HW11,November 26, 2021
"""

#1
class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

#2
class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed
        self.tricks = []


#3
class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed
        self.tricks = []
        
    def teach(self, trick):
        self.tricks.append(trick)
        print(f"{self.name} knows {trick}")

#4
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



#5
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


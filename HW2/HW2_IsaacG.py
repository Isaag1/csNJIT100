"""
Isaac Guerrero
CS 100 2018S Section 004
HW 02, January 24, 2018
"""

#1.
grades = ['A','F','C','F','A','B','A','C','A','B']
FREQUENCY = [grades.count('A'),grades.count('B'),grades.count('C'),grades.count('D'),grades.count('F')]
print(FREQUENCY)

#2.
dog_breeds = ['collie', 'sheepdog', 'Chow','Chihuahua']
hearing_dogs = dog_breeds[0:2]
tiny_dogs = [dog_breeds[-1]] 
print(hearing_dogs)
print(tiny_dogs)

print('Persian' in dog_breeds)


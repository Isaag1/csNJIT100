"""
Isaac Guerrero
CS 100 Section 015
HW05, October 10, 2021
"""

# Q1: 
months = ['January', 'February', 'March', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
for month in months:
    if month[0] == 'J':
        print(month)

# Q2: 
div = []
for x in range(0, 100):
    if x % 10 == 0:
        div.append(str(x))
print(div)

# Q3:
horton = "A person's a person, no matter how small."
vowels = "aeiouAEIOU"
for letter in horton:
    if letter in vowels:
        print(letter, end=' ')

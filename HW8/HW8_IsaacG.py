"""
Isaac Guerrero
CS 100 Section 015
HW08,November 7, 2021
"""
# 1
def twoWords(length, firstLetter):
    while True:
        first = input("Enter a {}-letter word please: ".format(length))
        if len(first) == length:
            break
    while True:
        second = input("Enter a word beginning with {} please: ".format(firstLetter))
        if second[0] == firstLetter.upper() or second[0] == firstLetter.lower():
            break
    return [first, second]

print(twoWords(4, 'B'))



# 2

def twoWordsV2(length, firstLetter):
    first = input("Enter a {}-letter word please: ".format(length))
    while len(first) != length:
        first = input("Enter a {}-letter word please: ".format(length))
    second = input("Enter a word beginning with {} please: ".format(firstLetter))
    while not second.lower().startswith(firstLetter.lower()):
        second = input("Enter a word beginning with {} please: ".format(firstLetter))
    return [first, second]

print(twoWordsV2(4, 'B'))


# 3


def enterNewPassword():
    while True:
        password = input("Enter a password with 8-15 characters, including at least one digit: ")
        if len(password) < 8 or len(password) > 15:
            print("Password must be between 8 and 15 characters")
        elif not any(char.isdigit() for char in password):
            print("Password must contain at least one digit")
        else:
            return password

print(enterNewPassword())


# 4
import random

def guessNumber():
    number = random.randint(0, 50)
    print("I'm thinking of a number in the range 0-50. You have five tries to guess it.")
    for i in range(1, 6):
        guess = int(input("Guess {}? ".format(i)))
        if guess == number:
            print("You are right! I was thinking of {}!".format(number))
            return
        elif guess < number:
            print("{} is too low".format(guess))
        else:
            print("{} is too high".format(guess))
    print("Sorry, you ran out of guesses. The number was {}.".format(number))

guessNumber()


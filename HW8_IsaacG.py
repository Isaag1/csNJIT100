"""
Isaac Guerrero
CS 100 Section 015
HW08,November 7, 2021
"""
# 1
import random
def twoWords(length, firstLetter):
    word1 = ''
    while len(word1) != length:
        word1 = input(f"Enter a {length}-letter word please: ")
    word2 = ''
    while not word2.startswith(firstLetter.lower()) and not word2.startswith(firstLetter.upper()):
        word2 = input(f"Enter a word beginning with {firstLetter} please: ")
    return [word1, word2]



# 2


def twoWordsV2(length, firstLetter):
    word1 = ''
    word2 = ''
    while len(word1) != length or not word2.startswith(firstLetter.lower()) and not word2.startswith(firstLetter.upper()):
        if len(word1) != length:
            word1 = input(f"Enter a {length}-letter word please: ")
        elif not word2.startswith(firstLetter.lower()) and not word2.startswith(firstLetter.upper()):
            word2 = input(f"Enter a word beginning with {firstLetter} please: ")
    return [word1, word2]


# 3


def enterNewPassword():
    while True:
        password = input("Enter a password between 8-15 characters that contains at least one digit: ")
        if len(password) < 8 or len(password) > 15:
            print("Password must be between 8-15 characters.")
        elif not any(char.isdigit() for char in password):
            print("Password must contain at least one digit.")
        else:
            print("Password accepted.")
            break



# 4
import random

def GuessNumber():
    num = random.randint(0, 50)
    print("I'm thinking of a number in the range 0-50. You have five tries to guess it.")
    for i in range(5):
        guess = int(input(f"Guess {i+1}? "))
        if guess == num:
            print(f"You are right! I was thinking of {num}!")
            return
        elif guess > num:
            print(f"{guess} is too high")
        else:
            print(f"{guess} is too low")
    print(f"Sorry, you did not guess the number. It was {num}.")

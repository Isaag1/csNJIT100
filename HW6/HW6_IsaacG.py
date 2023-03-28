"""
Isaac Guerrero
CS 100 Section 015
HW06,October 19, 2021
"""
# Q1:
def hasFinalLetter(strList, letter):
    strList2 = []
    for string in strList:
        if string[-1] in letter:
            strList2.append(string)
    return strList2 

test1 = ["hi", "bye", "hey"]
tester1 = "oey"
print(hasFinalLetter(test1, tester1))

test2 = ["hello", "welcome", "howdy"]
tester2 = "oye"
print(hasFinalLetter(test2, tester2))

test3 = ["Isaac", "Steven", "John"]
tester3 = "eiu"
print(hasFinalLetter(test3, tester3))


# Q2:
def isDivisible(maxInt, twoInts):
    divisibleList = []
    for num in range(1, maxInt):
        if num % twoInts[0] == 0 and num % twoInts[1] == 0:
            divisibleList.append(num)
    return divisibleList

a = 6
b = (1, 2)
print(isDivisible(a, b))

e = 10
f = (3, 2)
print(isDivisible(e, f))

c = 1
d = (1, 2)
print(isDivisible(c, d))

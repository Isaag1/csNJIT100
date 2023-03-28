"""
Isaac Guerrero
CS 100 Section 015
HW08,November 7, 2021
"""
#1
def safeOpen(filename):
    try:
        return open(filename)
    except FileNotFoundError:
        return None
#2
def safeFloat(n):
    try:
        return float(n)
    except ValueError:
        return 0.0      
print(safeFloat('abc'))
print(safeFloat('1'))

#3
def averageSpeed():
    count = 0
    file = None
    while count != 2:
        filename = input("Enter file name: ")
        file = safeOpen(filename)
        if file:
            break
        count = count + 1
        if count <= 1:
            print("Please try again.")
        if count == 2:
            print(" Yet another human error. Goodbye....")
            exit(0)
if __name__ == "__main__":
   averageSpeed()

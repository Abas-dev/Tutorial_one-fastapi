#This file is to practice list comprehension. 

def squareNum(num):
    return num ** 2

numbersList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

squared_numbers = list(map(squareNum, numbersList))

print (squared_numbers)
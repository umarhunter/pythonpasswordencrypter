import getpass
import random

def convert2ascii(string):
    return " ".join(str(ord(char)) for char in string)

def convert2string(number):
    return chr(number)

def createsmall():
    print("DEBUG: createsmall function launched")
    foo = input("Please enter the password you want to encrypt: ")
    newfoo = convert2ascii(foo)
    print("DEBUG: convert2ascii returned: ", newfoo)
    splitfoo = newfoo.split(" ")
    int_list = [int(x) for x in splitfoo]
    print(int_list)
    for i in range(len(int_list)):
        listvar = convert2string(int_list[i])
def createmedium():
    print("DEBUG: createmedium function launched")
    foo = input("Please enter the password you want to encrypt: ")
    newfoo = convert2ascii(foo)
    print("DEBUG: convert2ascii returned: ", newfoo)

def createlarge():
    print("DEBUG: createlarge function launched")
    foo = input("Please enter the password you want to encrypt: ")
    newfoo = convert2ascii(foo)
    print("DEBUG: convert2ascii returned: ", newfoo)

def createformulas():
    print("DEBUG: createformulas function launched")
    incrementvar = 1
    while incrementvar > 0:
        print("Please enter encryption length (1,2,3) ")
        userInput = input("1. Small\n2. Medium\n3. Large\nEnter here: ")
        if userInput == "1":
            incrementvar = -1
            createsmall()
        elif userInput == "2":
            incrementvar = -1
            createmedium()
        elif userInput == "3":
            incrementvar = -1
            createlarge()
        else:
            print("Invalid input, please enter: 1, 2, or 3")


def passwordfunction():
    useralgorithm = input("Please enter the password you want to encrypt: ")


if __name__ == '__main__':
    username = getpass.getuser()
    print("Python Password Manager V1")
    print("..........................")
    info = open('information.txt', 'w+')

    print("Welcome, ", username)
    formulas = input("Will you require pre-determined formulas? y/n:")
    if formulas == "y":
        createformulas()
    elif formulas == "n":
        passwordfunction()

import getpass
import random

def convert2ascii(string, num):
    return " ".join(str(ord(char) + num) for char in string)


def convert2string(number):
    return chr(number)


def randomizer(param):
    if param == 1:
        return random.randint(1,4)
    elif param == 2:
        return random.randint(4, 8)
    else:
        return random.randint(9, 18)


def createsmall():
    # print("DEBUG: createsmall function launched")
    foo = input("Please enter the password you want to encrypt: ")
    newfoo = convert2ascii(foo, randomizer(1))
    # print("DEBUG: convert2ascii returned: ", newfoo)
    splitfoo = newfoo.split(" ")
    integer_list = [int(x) for x in splitfoo]
    # print("DEBUG: int_list: ", integer_list)
    appendvar = []
    for i in range(len(integer_list)):
        appendvar.append(str(convert2string(integer_list[i])))
    print("Your new password is: ", "".join(appendvar))

def createmedium():
    # print("DEBUG: createsmall function launched")
    foo = input("Please enter the password you want to encrypt: ")
    newfoo = convert2ascii(foo, randomizer(2))
    # print("DEBUG: convert2ascii returned: ", newfoo)
    splitfoo = newfoo.split(" ")
    integer_list = [int(x) for x in splitfoo]
    # print("DEBUG: int_list: ", integer_list)
    appendvar = []
    for i in range(len(integer_list)):
        appendvar.append(str(convert2string(integer_list[i])))
    print("Your new password is: ", "".join(appendvar))

def createlarge():
    # print("DEBUG: createsmall function launched")
    foo = input("Please enter the password you want to encrypt: ")
    newfoo = convert2ascii(foo, randomizer(3))
    # print("DEBUG: convert2ascii returned: ", newfoo)
    splitfoo = newfoo.split(" ")
    integer_list = [int(x) for x in splitfoo]
    # print("DEBUG: int_list: ", integer_list)
    appendvar = []
    for i in range(len(integer_list)):
        appendvar.append(str(convert2string(integer_list[i])))
    print("Your new password is: ", "".join(appendvar))

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
    print("Python Password Manager V2")
    print("..........................")
    print("WARNING: AS OF NOW, ONLY PRE-DETERMINED FORMULAS ARE WORKING")
    #info = open('information.txt', 'w+') // keeping in case of future implementation with file systems

    print("Welcome, ", username)
    increment = 1
    while(increment > 0):
        formulas = input("Will you require pre-determined formulas? y/n:")
        if formulas == "y":
            increment = -1
            createformulas()
        elif formulas == "n":
            increment = -1
            passwordfunction()
        else:
            print("Please enter a valid input: (y/n)")
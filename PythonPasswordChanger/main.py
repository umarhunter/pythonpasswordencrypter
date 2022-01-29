import getpass
import random
import sys
import time
import webbrowser


def convert2ascii(string, num):
    return " ".join(str(ord(char) + num) for char in string)


def convert2string(number):
    return chr(number)


def randomizer(param):
    if param == 1:
        return random.randint(1, 4)
    elif param == 2:
        return random.randint(4, 8)
    else:
        return random.randint(9, 18)


def add2file(passw, rand):
    file = open("information.txt", "a")
    thetime = time.asctime(time.localtime(time.time()))
    file.write("Password: " + passw + "\nTimestamp: " + thetime + "\nAlgorithm: " + str(rand))
    file.close()


def createsmall():
    # print("DEBUG: createsmall function launched")
    foo = input("Please enter the password you want to encrypt: ")
    randomreturn = randomizer(1)
    # print("DEBUG: randomreturn: ", randomreturn)
    newfoo = convert2ascii(foo, randomreturn)
    # print("DEBUG: convert2ascii returned: ", newfoo)
    splitfoo = newfoo.split(" ")
    integer_list = [int(x) for x in splitfoo]
    # print("DEBUG: int_list: ", integer_list)
    appendvar = []
    for i in range(len(integer_list)):
        appendvar.append(str(convert2string(integer_list[i])))
    var = "".join(appendvar)
    print("Your new password is: ", var)
    add2file(var, randomreturn)


def createmedium():
    # print("DEBUG: createsmall function launched")
    foo = input("Please enter the password you want to encrypt: ")
    randomreturn = randomizer(2)
    # print("DEBUG: randomreturn: ", randomreturn)
    newfoo = convert2ascii(foo, randomreturn)
    # print("DEBUG: convert2ascii returned: ", newfoo)
    splitfoo = newfoo.split(" ")
    integer_list = [int(x) for x in splitfoo]
    # print("DEBUG: int_list: ", integer_list)
    appendvar = []
    for i in range(len(integer_list)):
        appendvar.append(str(convert2string(integer_list[i])))
    var = "".join(appendvar)
    print("Your new password is: ", var)
    add2file(var, randomreturn)


def createlarge():
    # print("DEBUG: createsmall function launched")
    foo = input("Please enter the password you want to encrypt: ")
    randomreturn = randomizer(3)
    # print("DEBUG: randomreturn: ", randomreturn)
    newfoo = convert2ascii(foo, randomreturn)
    # print("DEBUG: convert2ascii returned: ", newfoo)
    splitfoo = newfoo.split(" ")
    integer_list = [int(x) for x in splitfoo]
    # print("DEBUG: int_list: ", integer_list)
    appendvar = []
    for i in range(len(integer_list)):
        appendvar.append(str(convert2string(integer_list[i])))
    var = "".join(appendvar)
    print("Your new password is: ", var)
    add2file(var, randomreturn)


def createformulas():
    # print("DEBUG: createformulas function launched")
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
            print("Invalid input, please try again!")


def passwordfunction():
    useralgorithm = input("Please enter the password you want to encrypt: ")


def findthatkey(string,num):
    newfoo = convert2ascii(string, num)
    splitfoo = newfoo.split(" ")
    integer_list = [int(x) for x in splitfoo]
    appendvar = []
    for i in range(len(integer_list)):
        appendvar.append(str(convert2string(integer_list[i])))
    var = "".join(appendvar)
    return var

def findkey():
    print("Welcome to the Password Recovery Program!")
    print("Please note: You must know your original password and formula in order to get the encrypted one. Otherwise, "
          "there is no way of getting it.")
    whilevar = 1
    while whilevar > 0:
        choice = input("Do you have your original password? y/n: ")
        if choice == "n":
            whilevar = -1
            tips = input("Sorry you couldn't remember your original password. Would you like some tips on remembering "
                         "passwords? y/n: ")
            if tips == "y":
                webbrowser.open("https://www.wikihow.com/Remember-a-Forgotten-Password")
            else:
                print("Have a nice day!")
                sys.exit()
        elif choice == "y":
            whilevar = -1
        else:
            print("Invalid input. Please try again.")
    original = input("Please enter your original password: ")
    formula = int(input("Please enter your formula #: "))
    encrypt = findthatkey(original, formula)
    print("Your encrypted password was: ", encrypt)
    save = input("Would you like to save this password into text file? y/n: ")
    if save == "y":
        add2file(encrypt, formula)
    else:
        print("Have a nice day!")

def createpassword():
    increment = 1
    while increment > 0:
        formulas = input("Will you require pre-determined formulas? y/n:")
        if formulas == "y":
            increment = -1
            createformulas()
        elif formulas == "n":
            increment = -1
            passwordfunction()
        else:
            print("Please enter a valid input: (y/n)")


if __name__ == '__main__':
    username = getpass.getuser()
    print("Python Password Manager V3")
    print("..........................")
    print("WARNING: AS OF NOW, ONLY PRE-DETERMINED FORMULAS ARE WORKING")
    print("..........................\n")
    info = open('information.txt', 'w+')

    print("Welcome, ", username, "\n")
    firstincrement = 1
    while firstincrement > 0:
        print("Please select your choice:\n1) Create new password\n2) Find my password using key")
        firstchoice = input("Please enter 1 or 2: ")
        if firstchoice == "2":
            firstincrement = -1
            findkey()
        elif firstchoice == "1":
            firstincrement = -1
            createpassword()
        else:
            print("Invalid input, please try again!")

import getpass
import random
import sys
import time
import webbrowser


def convert2ascii(string, num):
    blank = ""
    for index in range(len(string)):
        whilevar = ord(string[index]) + num
        while whilevar > 122:
            whilevar = whilevar - 26
        bar = whilevar
        blank = blank + chr(bar)
    return blank


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
    file.write(
        "User: " + getpass.getuser() + "\nPassword: " + passw + "\nTimestamp: " + thetime + "\nAlgorithm: " + str(rand))
    file.close()
    print("Successfully saved content to file\n")
    whilevar = 1
    while whilevar > 0:
        openfile = input("Would you like to open the file now? y/n:")
        if openfile == "y":
            whilevar = -1
            secondwhilevar = 1
            while secondwhilevar > 0:
                texteditor = input(
                    "How would you prefer reading the file?\n1) Here in the Python terminal\n2) Default text "
                    "editor\nPlease enter 1 or 2: ")
                if texteditor == "1":
                    secondwhilevar = -1
                    tfile = open("information.txt", "r")
                    print(tfile.read())
                elif texteditor == "2":
                    secondwhilevar = -1
                    webbrowser.open("information.txt")
                else:
                    print("Invalid input. Please try again.")
        elif openfile == "n":
            whilevar = -1
            print("Have a nice day!")
        else:
            print("Invalid input. Please try again.")


def process(randomvar):
    truee = 1
    while truee == 1:
        userinput = input("Please enter the password you want to encrypt: ")
        print("You have entered: ", userinput)
        verify = input("Is this correct? y/n: ")
        if verify == "y":
            truee = 0
        elif verify == "n":
            print("\n")
        else:
            print("Invalid input. Please try again.")
    randomreturn = randomizer(randomvar)
    # print("DEBUG: randomreturn: ", randomreturn)
    newinput = convert2ascii(userinput, randomreturn)

    print("Your new password is: ", newinput)
    whilevar = 1
    while whilevar > 0:
        savefile = input("Would you like to save this password to a text file? y/n: ")
        if savefile == "y":
            whilevar = -1
            add2file(newinput, randomreturn)
        elif savefile == "n":
            whilevar = -1
            print("Thank you for using this program!")
        else:
            print("Invalid input. Please try again.")


def createsmall():
    process(1)


def createmedium():
    process(2)


def createlarge():
    process(3)


def createformulas():
    # print("DEBUG: createformulas function launched")
    incrementvar = 1
    while incrementvar > 0:
        print("Please enter encryption length (1,2,3) ")
        userinput = input("1. Small\n2. Medium\n3. Large\nEnter here: ")
        if userinput == "1":
            incrementvar = -1
            createsmall()
        elif userinput == "2":
            incrementvar = -1
            createmedium()
        elif userinput == "3":
            incrementvar = -1
            createlarge()
        else:
            print("Invalid input. Please try again.")


def passwordfunction():
    truee = 1
    while truee == 1:
        useralgorithm = input("Please enter the password you want to encrypt: ")
        print("You have entered: ", useralgorithm)
        verify = input("Is this correct? y/n: ")
        if verify == "y":
            truee = 0
        elif verify == "n":
            print("\n")
        else:
            print("Invalid input. Please try again.")
    ordvar = int(input("Select ord value: "))
    newinput = convert2ascii(useralgorithm, ordvar)
    print("Your new password is: ", newinput)
    whilevar = 1
    while whilevar > 0:
        savefile = input("Would you like to save this password to a text file? y/n: ")
        if savefile == "y":
            whilevar = -1
            add2file(newinput, ordvar)
        elif savefile == "n":
            whilevar = -1
            print("Thank you for using this program!")
        else:
            print("Invalid input. Please try again.")


def findthatkey(string, num):
    integer_list = convert2ascii(string, num)
    return integer_list


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
                         "passwords?\nWarning: Link will open in browser if accepted\ny/n: ")
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
    save = input("Would you like to save this password into a text file? y/n: ")
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
    print("Python Password Manager V5")
    print("..........................")
    print("   MADE BY: UMAR FARUQUE  ")
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

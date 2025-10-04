
###### EASTER EGGS ######

if __name__ == "__main__":
    print("Error: please execute 'start.py' to start Dumbass Calculator")
    exit()

def credit():
    with open("dependencies/god.jpg", "r") as f:
        text = f.read()
    temp = ""
    for ch in text:
        for i in string.printable:
            if i == ch or i == temp:
                time.sleep(0.01)
                print(temp + i)
                temp += ch
                break
            else:
                time.sleep(0.01)
                print(temp + i)
    time.sleep(3)
    start()

def ranNumGen():
    print("\nRandom Number Generator")
    num = input("Generate a number within (First Number, Last Number): ").lower()
    if num == "stop":
        stop()
    elif num == "back":
        start()
        return
    elif is_valid_expression(num):
        num = eval(num)
        ranNum = random.randint(num[0], num[1])
        print(f"\nThe number generated is {ranNum}\n")
        Eggmarker.ranNumWrite(num, ranNum)
        res = input("Would you like to generate another? (y/n): ").lower()
        if res == "y":
            ranNumGen()
        elif res == "n":
            start()
        else:
            print("the function you selected does not exist, please check your intelligence and try again")
            dumb_restart()
    else:
        print("*syntax error*")
        print("your lack of intelligence has resulted in errors")
        dumb_restart()

def iloveyou():
    heart = r"""
⠀⠀⠀⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⠀⠀⠀⠀
⠀⢈⣷⡿⣿⠿⢷⣦⣆⠀⣰⣤⣶⠿⢿⣿⣷⡇⠀⠀
⠀⣾⡿⠃⠈⠀⠀⢈⣿⣿⣿⡁⠀⠀⠀⠀⢻⣿⡀⠀
⠲⣿⡷⠀⠀⠀⠀⠘⢀⡿⡅⠙⠀⠀⠀⠀⢺⣿⡿⠂
⠛⢻⣿⡃⠀⠀⠀⠀⠘⢀⡇⠀⠀⠀⠀⠀⣿⡿⠛⠀
⠀⢈⣿⣿⣁⠀⠀⠀⠀⠈⠀⠀⠀⠀⣀⣽⣿⣃⠀⠀
⠀⠀⠀⠿⣿⣷⡀⡀⠀⠀⠀⢠⡀⣴⢿⡟⠇⠀⠀⠀
⠀⠀⠀⠀⠈⠻⢿⣷⡞⠀⢲⣾⡿⠿⠁⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠘⠉⠛⣷⡛⠁⠘⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢸⠁⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠓⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    """
    for i in heart.splitlines():
        time.sleep(0.2)
        print(i)
    time.sleep(0.5)
    print("Your love for Dumbass Calculator is appreciated")
    time.sleep(3)
    start()

def starStripes():
    print("You wanna see smth cool?")
    time.sleep(1)
    print("Alright here you go :)")
    time.sleep(1)
    with open("dependencies/settings.json", "r") as f:
        settings = json.load(f)
    loop = 0
    while loop < 3:
        for i in range(settings["line_size"] - 1):
            stars = 1
            for j in range(i):
                stars += 1
            print("*" * stars)
            time.sleep(0.01)
        for i in range(settings["line_size"] - 1):
            stars = settings["line_size"]
            for j in range(i):
                stars -= 1
            spaces = settings["line_size"] - stars
            print(" " * spaces + "*" * stars)
            time.sleep(0.01)
        for i in range(settings["line_size"] - 1):
            stars = 1
            for j in range(i):
                stars += 1
            spaces = settings["line_size"] - stars
            print(" " * spaces + "*" * stars)
            time.sleep(0.01)
        for i in range(settings["line_size"] - 1):
            stars = settings["line_size"]
            for j in range(i):
                stars -= 1
            print("*" * stars)
            time.sleep(0.01)
        loop += 1
    time.sleep(1)
    print("Cool right?")
    time.sleep(1)
    print("Anyways, get your ass back to math")
    time.sleep(1)
    start()

import time
import string
import random
import json
from .main import start, stop, dumb_restart
from .checks import is_valid_expression
from .recwriter import Eggmarker
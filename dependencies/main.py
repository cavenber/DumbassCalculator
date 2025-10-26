
###### MAIN ######

if __name__ == "__main__":
    print("Error: please execute 'start.py' to start Dumbass Calculator")
    exit()

def start():
    with open("dependencies/settings.json") as f:
        settings = json.load(f)
    print("-" * settings['line_size'])
    # inputs
    program = input("Please select a program (1-10) ('help' for assistance): ").lower()
    # options (here decides what the user needs to type to get into each program)
    if program == "stop":
        stop()
    elif program == "back":
        print("Where the fuck you wanna go back to this is the start")
        rst = input("Let's start over shall we? (y/n): ").lower()
        if rst == "y":
            start()
        elif rst == "n":
            print("alr bye")
            stop()
        else:
            print("the program you selected does not exist, please check your intelligence and try again")
            dumb_restart()
    elif program == "help":
        print(r"""
How to Use Dumbass Calculator:
    Enter the numbers you have that matches the variables
    For an unknown variable enter a "x" or a "." or whatever
    Enter "(ans)", "(x1)" or "(x2)" to use the answer of your previous calculation

Functions:
    setting: Configure Dumbass Calculator
    rng: Random Number Generator

Command List:
    stop: Put a stop to Dumbass Calculators plans
    back: Go back to the last input

Program List:
    1: Arithmetic Operation
    2: Quadratic Equation
    3: Variation
    4: Arithmetic Sequence/Series & Geometric Sequence/Series
    5: Coordinate Geometry
    6: Triangular Calculation
    7: Probability Calculation
    8: Set Operation
    9: Decimal & Binary Conversion
    10: Caesar Cipher Encoder
""")
        start()
    # portals
    elif program == "factory reset":
        factory_reset()
    elif program == "setting":
        setting()
    elif program == "credit":
        credit()
    elif program == "rng":
        ranNumGen()
    elif program == "i love you":
        iloveyou()
    elif program == "i wanna see stars" or program == "i want to see stars":
        starStripes()
    elif program == "1":
        arithmetic_operation()
    elif program == "2":
        quadratic_equation()
    elif program == "3":
        variation()
    elif program == "4":
        arithmetic_or_geometric_s()
    elif program == "5":
        coordinate_geometry()
    elif program == "6":
        triangular_calculation()
    elif program == "7":
        probability_calculation()
    elif program == "8":
        set_operation()
    elif program == "9":
        dec_bin_conversion()
    elif program == "10":
        caesar_cipher_encoder()
    else:
        print("\nthe program you selected does not exist, please check your intelligence and try again")
        dumb_restart()

# stop function duh
def stop():
    records()
    print("Have a pleasant day")
    cleaner()
    sys.exit()

# standard restart
def restart():
    with open("dependencies/settings.json", "r") as f:
        settings = json.load(f)
    if settings['auto_restart'] == "true":
        start()
    elif settings['auto_restart'] == "false":
        print("Thank you for using Dumbass Calculator")
        restart_in = input("Would you like to do another calculation? (y/n): ").lower()
        if restart_in == "y":
            start()
        elif restart_in == "n":
            stop()
        else:
            print("\nthe function you selected does not exist, please check your intelligence and try again")
            dumb_restart()

# the restart if you entered smth dumb
def dumb_restart():
    print("\nI hope you have improved from your previous idiotic actions")
    restart_in = input("Would you like to try again? (y/n): ").lower()
    if restart_in == "y":
        start()
    elif restart_in == "n":
        records()
        print("you are nothing but a mindless meat-bag")
        cleaner()
        sys.exit()
    else:
        print("\nreally... again...")
        print("you are one of the reasons humans are doomed to extinct")
        cleaner()
        sys.exit()

# this shows all the calculations made in a session
def records():
    with open("dependencies/settings.json") as f:
        settings = json.load(f)
    print(f"\n{'=' * settings['line_size']}\n"
        "Calculation Records:")
    with open("dependencies/records.txt", "r") as f:
        print(f.read())

def cleaner():
    with open("dependencies/records.txt", "w") as f:
        f.write("")
    with open("dependencies/data.json", "r") as f:
        data = json.load(f)
    data['ans'] = "0"
    data['x1'] = "0"
    data['x2'] = "0"
    with open("dependencies/data.json", "w") as f:
        json.dump(data, f)

def setting():
    with open("dependencies/settings.json", "r") as f:
        settings = json.load(f)
    while True:
        print("\nSettings\n")
        print("default: Restores all settings to default\n"
              f"1: Auto Restart = {settings['auto_restart']}\n"
              f"2: Line Size = {settings['line_size']}\n")
        change = input("Which setting would you like to change? (1-2): ").lower()
        if change == "stop":
            stop()
        elif change == "back":
            start()
            return
        elif change == "default":
            value = input("Are you sure? (y/n): ").lower()
            if value == "stop":
                stop()
            elif value == "back":
                continue
            break
        elif change == "1":
            value = input("What would you like to change it to? (true/false): ").lower()
            if value == "stop":
                stop()
            elif value == "back":
                continue
            break
        elif change == "2":
            value = input("What would you like to change it to? (enter int): ").lower()
            if value == "stop":
                stop()
            elif value == "back":
                continue
            break
        else:
            break
    if change == "default":
        if value == "y":
            settings['auto_restart'] = "false"
            settings['line_size'] = 44
            with open("dependencies/settings.json", "w") as f:
                json.dump(settings, f)
            print("\nAll settings has been restored to default\n")
            start()
    elif change == "1":
        if value == "true":
            settings['auto_restart'] = "true"
            with open("dependencies/settings.json", "w") as f:
                json.dump(settings, f)
            print(f"\nAuto Restart has been changed to {settings['auto_restart']}\n")
            start()
        elif value == "false":
            settings['auto_restart'] = "false"
            with open("dependencies/settings.json", "w") as f:
                json.dump(settings, f)
            print(f"\nAuto Restart has been changed to {settings['auto_restart']}\n")
            start()
        else:
            print("\n*syntax error*")
            print("your lack of intelligence has resulted in errors")
            dumb_restart()
    elif change == "2":
        if is_valid_int(value):
            value = int(value)
            if value >= 42:
                settings['line_size'] = value
                with open("dependencies/settings.json", "w") as f:
                    json.dump(settings, f)
                print(f"\nLine Size has been changed to {settings['line_size']}\n")
                start()
            else:
                print("\nIt would not look good, trust me\n")
                start()
        else:
            print("\n*syntax error*")
            print("your lack of intelligence has resulted in errors")
            dumb_restart()
    else:
        print("\n*syntax error*")
        print("your lack of intelligence has resulted in errors")
        dumb_restart()

def factory_reset():
    confirmation = input("Are you sure you want to factory reset? (y/n): ").lower()
    if confirmation == "y":
        with open("dependencies/records.txt", "w") as f:
            f.write("")
        with open("dependencies/settings.json", "r") as f:
            settings = json.load(f)
        settings['auto_restart'] = "false"
        settings['line_size'] = 44
        cleaner()
        print("\nFactory reset successful\n")
        start()
    elif confirmation == "n":
        print("\nOkay, I hope you dont play with my heart like that again\n")
        start()
    else:
        print("\n*syntax error*")
        print("your lack of intelligence has resulted in errors")
        dumb_restart()

import sys
import json
from .checks import is_valid_int
from .lobby import variation, arithmetic_or_geometric_s, coordinate_geometry, triangular_calculation, probability_calculation
from .eggs import credit, ranNumGen, iloveyou, starStripes
from calculators.basic_cals import arithmetic_operation, quadratic_equation, set_operation, dec_bin_conversion, caesar_cipher_encoder
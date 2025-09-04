
###### MAIN ######

def start():
    print("--------------------------------------------")
    # inputs
    program = input("Please select a program (1-9) ('help' for assistance): ").lower()
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
        print("\nHow to Use Dumbass Calculator:\n"
            "Enter the numbers you have that matches the variables\n"
            "For an unknown variable enter a 'x' or a '.' or whatever\n"
            "\nProgram list:\n"
            "1: Arithmetic Operation\n"
            "2: Quadratic Equation\n"
            "3: Variation\n"
            "4: Arithmetic Sequence/Series & Geometric Sequence/Series\n"
            "5: Coordinate Geometry\n"
            "6: Triangular Calculation\n"
            "7: Probability Calculation\n"
            "8: Set Operation\n"
            "9: Decimal & Binary Conversion\n"
            "\nFunctions:\n"
            "setting: Configure Dumbass Calculator\n"
            "rng: Random Number Generator\n"
            "\nCommand list:\n"
            "stop: Put a stop to Dumbass Calculators plans\n"
            "back: Go back to the last input")
        start()
    # portals
    elif program == "setting":
        settings()
    elif program == "credit":
        credit()
    elif program == "rng":
        ranNumGen()
    elif program == "i love you":
        iloveyou()
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
    else:
        print("\nthe program you selected does not exist, please check your intelligence and try again")
        dumb_restart()

# stop function duh
def stop():
    records()
    print("Have a pleasant day")
    sys.exit()

# standard restart
def restart():
    with open("dependencies/settings.json", "r") as f:
        settings_info = json.load(f)
    if settings_info['auto_restart'] == "true":
        start()
    elif settings_info['auto_restart'] == "false":
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
        sys.exit()
    else:
        print("\nreally... again...")
        print("you are one of the reasons humans are doomed to extinct")

# this shows all the calculations made in a session
def records():
    print("\n============================================\n"
        "Calculation Records:")
    with open("dependencies/records.txt", "r") as f:
        print(f.read())

def settings():
    with open("dependencies/settings.json", "r") as f:
        settings_info = json.load(f)
    while True:
        print("\nSettings")
        print(f"1: Auto Restart = {settings_info['auto_restart']}\n")
        change = input("Which setting would you like to change? (1): ").lower()
        if change == "stop":
            stop()
        elif change == "back":
            start()
            return
        elif change == "1":
            value = input("What would you like to change it to? (true/false): ").lower()
            if value == "stop":
                stop()
            elif value == "back":
                continue
            break
        else:
            break
    if change == "1":
        if value == "true":
            settings_info['auto_restart'] = "true"
            with open("dependencies/settings.json", "w") as f:
                json.dump(settings_info, f)
            start()
        elif value == "false":
            settings_info['auto_restart'] = "false"
            with open("dependencies/settings.json", "w") as f:
                json.dump(settings_info, f)
            start()
        else:
            print("\n*syntax error*")
            print("your lack of intelligence has resulted in errors")
            dumb_restart()
    else:
        print("\n*syntax error*")
        print("your lack of intelligence has resulted in errors")
        dumb_restart()

import sys
import json
from .lobby import variation, arithmetic_or_geometric_s, coordinate_geometry, triangular_calculation, probability_calculation
from .eggs import credit, ranNumGen, iloveyou
from calculators.basic_cals import arithmetic_operation, quadratic_equation, set_operation, dec_bin_conversion
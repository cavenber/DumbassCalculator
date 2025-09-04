
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
            "\nCommand list:\n"
            "stop: Put a stop to dumbass calculators plans\n"
            "back: Go back to the last input")
        start()
    # portals
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

import sys
from .lobby import variation, arithmetic_or_geometric_s, coordinate_geometry, triangular_calculation, probability_calculation
from .eggs import credit, ranNumGen, iloveyou
from calculators.basic_cals import arithmetic_operation, quadratic_equation, set_operation, dec_bin_conversion
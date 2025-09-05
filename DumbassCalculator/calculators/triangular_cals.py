
if __name__ == "__main__":
    print("Error: please execute 'start.py' to start Dumbass Calculator")
    exit()

import math
from dependencies.main import stop, restart, dumb_restart
from dependencies.checks import is_valid_equation
from dependencies.lobby import triangular_calculation
from dependencies.recwriter import Recwriter

def pythagorean_theorem():
    while True:
        print("\nPythagorean Theorem")
        # inputs
        a = input("Please enter your a: ").lower()
        if a == "stop":
            stop()
        elif a == "back":
            triangular_calculation()
            return
        b = input("Please enter your b: ").lower()
        if b == "stop":
            stop()
        elif b == "back":
            continue
        c = input("Please enter your c: ").lower()
        if c == "stop":
            stop()
        elif c == "back":
            continue
        break
    # verifications
    if is_valid_equation(a) and is_valid_equation(b):
        a = eval(a)
        b = eval(b)
        # calculations
        c = ((a ** 2) + (b ** 2)) ** 0.5
        print(f"\nc = {c}\n")
        Recwriter.ptp6a(a, b, c)
        restart()
    # verifications
    elif is_valid_equation(a) and is_valid_equation(c):
        a = eval(a)
        c = eval(c)
        # calculations
        b = ((c ** 2) - (a ** 2)) ** 0.5
        print(f"\nb = {b}\n")
        Recwriter.ptp6b(a, c, b)
        restart()
    # verifications
    elif is_valid_equation(b) and is_valid_equation(c):
        b = eval(b)
        c = eval(c)
        # calculations
        a = ((c ** 2) - (b ** 2)) ** 0.5
        print(f"\na = {a}\n")
        Recwriter.ptp6c(b, c, a)
        restart()
    else:
        print("\n*syntax error*")
        print("your lack of intelligence has resulted in errors")
        dumb_restart()

def sine_formula():
    while True:
        print("\nSine Formula")
        # inputs
        inA = input("Please enter your given angle: ").lower()
        if inA == "stop":
            stop()
        elif inA == "back":
            triangular_calculation()
            return
        ina = input("Please enter your given side: ").lower()
        if ina == "stop":
            stop()
        elif ina == "back":
            continue
        inB = input("Please enter your unknown angle: ").lower()
        if inB == "stop":
            stop()
        elif inB == "back":
            continue
        inb = input("Please enter your unknown side: ").lower()
        if inb == "stop":
            stop()
        elif inb == "back":
            continue
        break
    # verifications
    if is_valid_equation(inA) and is_valid_equation(ina) and is_valid_equation(inB):
        A = eval(inA)
        a = eval(ina)
        B = eval(inB)
        # calculations
        A = math.radians(A)
        B = math.radians(B)
        b = (a * math.sin(B)) / math.sin(A)
        print(f"\nUnknown Side = {b}\n")
        Recwriter.sfp6a(inA, ina, inB, b)
        restart()
    # verifications
    elif is_valid_equation(inA) and is_valid_equation(ina) and is_valid_equation(inb):
        A = eval(inA)
        a = eval(ina)
        b = eval(inb)
        # calculations
        A = math.radians(A)
        B = (math.sin(A) * b) / a
        B = math.degrees(math.asin(B))
        print(f"\nUnknown Angle = {B}\n")
        Recwriter.sfp6b(inA, ina, inb, B)
        restart()
    else:
        print("\n*syntax error*")
        print("your lack of intelligence has resulted in errors")
        dumb_restart()

def cosine_formula():
    while True:
        # input
        print("\nCosine Formula")
        ina = input("Please enter your given side: ").lower()
        if ina == "stop":
            stop()
        elif ina == "back":
            triangular_calculation()
            return
        inb = input("Please enter your given side: ").lower()
        if inb == "stop":
            stop()
        elif inb == "back":
            continue
        inC = input("Please enter your unknown angle: ").lower()
        if inC == "stop":
            stop()
        elif inC == "back":
            continue
        inc = input("Please enter your unknown side: ").lower()
        if inc == "stop":
            stop()
        elif inc == "back":
            continue
        break
    # verifications
    if is_valid_equation(ina) and is_valid_equation(inb) and is_valid_equation(inC):
        a = eval(ina)
        b = eval(inb)
        C = eval(inC)
        # calculations
        C = math.radians(C)
        c = ((a ** 2) + (b ** 2) - (2 * a * b * math.cos(C))) ** 0.5
        print(f"\nUnknown Side = {c}\n")
        Recwriter.cfp6a(ina, inb, inC, c)
        restart()
    # verifications
    elif is_valid_equation(ina) and is_valid_equation(inb) and is_valid_equation(inc):
        a = eval(ina)
        b = eval(inb)
        c = eval(inc)
        # calculations
        C = ((a ** 2) + (b ** 2) - (c ** 2)) / (2 * a * b)
        C = math.degrees(math.acos(C))
        print(f"\nUnknown Angle = {C}\n")
        Recwriter.cfp6b(ina, inb, inc, C)
        restart()
    else:
        print("\n*syntax error*")
        print("your lack of intelligence has resulted in errors")
        dumb_restart()
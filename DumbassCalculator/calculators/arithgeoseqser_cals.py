
if __name__ == "__main__":
    print("Error: please execute 'start.py' to start Dumbass Calculator")
    exit()

import math
from dependencies.main import stop, restart, dumb_restart
from dependencies.checks import is_valid_equation
from dependencies.lobby import arithmetic_or_geometric_s
from dependencies.recwriter import Recwriter

def arithmetic_sequence():
    while True:
        print("\nArithmetic Sequence")
        # inputs
        t1 = input("Please enter your T(1): ").lower()
        if t1 == "stop":
            stop()
        elif t1 == "back":
            arithmetic_or_geometric_s()
            return
        t2 = input("Please enter your T(2): ").lower()
        if t2 == "stop":
            stop()
        elif t2 == "back":
            continue
        n = input("Please enter your n: ").lower()
        if n == "stop":
            stop()
        elif n == "back":
            continue
        tn = input("Please enter your T(n): ").lower()
        if t2 == "stop":
            stop()
        elif t2 == "back":
            continue
        break
    # verifications
    if is_valid_equation(t1) and is_valid_equation(t2) and is_valid_equation(n): # given T(1), T(2) and n
        t1 = eval(t1)
        t2 = eval(t2)
        n = eval(n)
        # calculations
        a = t1
        d = t2 - t1
        tn = a + (n - 1) * d
        print(f"\nT({n}) = {tn}\n")
        Recwriter.asqp4a(t1, t2, n, tn)
        restart()
    # verifications
    elif is_valid_equation(t1) and is_valid_equation(t2) and is_valid_equation(tn): # given T(1), T(2) and T(n)
        t1 = eval(t1)
        t2 = eval(t2)
        tn = eval(tn)
        # calculations
        a = t1
        d = t2 - t1
        n = ((tn - a) / d) + 1
        print(f"n = {n}")
        Recwriter.asqp4b(t1, t2, tn, n)
        restart()
    elif is_valid_equation(t1) and is_valid_equation(t2): # only T(1) and T(2) are provided
        t1 = eval(t1)
        t2 = eval(t2)
        # calculations
        a = t1
        d = t2 - t1
        x = a + -d
        if x < 0:
            pxs = "-"
            px = -x
        else:
            pxs = "+"
            px = x
        print(f"\n{d} * n {pxs} {px}\n")
        Recwriter.asqp4c(t1, t2, d, pxs, px)
        restart()
    else:
        print("\n*syntax error*")
        print("your lack of intelligence has resulted in errors")
        dumb_restart()

def arithmetic_series():
    while True:
        print("\nArithmetic Series")
        # inputs
        t1 = input("Please enter your T(1): ").lower()
        if t1 == "stop":
            stop()
        elif t1 == "back":
            arithmetic_or_geometric_s()
            return
        t2 = input("Please enter your T(2): ").lower()
        if t2 == "stop":
            stop()
        elif t2 == "back":
            continue
        n = input("Please enter your n: ").lower()
        if n == "stop":
            stop()
        elif n == "back":
            continue
        tn = input("Please enter your T(n): ").lower()
        if tn == "stop":
            stop()
        elif n == "back":
            continue
        break
    # verifications
    if is_valid_equation(t1) and is_valid_equation(t2) and is_valid_equation(n): # given T(1), T(2) and n
        t1 = eval(t1)
        t2 = eval(t2)
        n = eval(n)
        # calculations
        a = t1
        d = t2 - t1
        sn = (n / 2) * (2 * a + (n - 1) * d)
        print(f"\nS({n}) = {sn}\n")
        Recwriter.asrp4a(t1, t2, n, sn)
        restart()
    # verifications
    elif is_valid_equation(t1) and is_valid_equation(t2) and is_valid_equation(tn): # given T(1), T(2) and T(n)
        t1 = eval(t1)
        t2 = eval(t2)
        tn = eval(tn)
        # calculations
        a = t1
        d = t2 - t1
        x = a + -d
        x = tn - x
        n = x / d
        sn = (n / 2) * (2 * a + (n - 1) * d)
        print(f"\nS({n}) = {sn}\n")
        Recwriter.asrp4b(t1, t2, tn, sn)
        restart()
    else:
        print("\n*syntax error*")
        print("your lack of intelligence has resulted in errors")
        dumb_restart()

def geometric_sequence():
    while True:
        print("\nGeometric Sequence")
        # inputs
        t1 = input("Please enter your T(1): ").lower()
        if t1 == "stop":
            stop()
        elif t1 == "back":
            arithmetic_or_geometric_s()
            return
        t2 = input("Please enter your T(2): ").lower()
        if t2 == "stop":
            stop()
        elif t2 == "back":
            continue
        n = input("Please enter your n: ").lower()
        if n == "stop":
            stop()
        elif n == "back":
            continue
        tn = input("Please enter your T(n): ").lower()
        if tn == "stop":
            stop()
        elif n == "back":
            continue
        break
    # verifications
    if is_valid_equation(t1) and is_valid_equation(t2) and is_valid_equation(n): # given T(1), T(2) and n
        t1 = eval(t1)
        t2 = eval(t2)
        n = eval(n)
        # calculations
        a = t1
        r = t2 / t1
        tn = a * (r ** (n - 1))
        print(f"\nT({n}) = {tn}\n")
        Recwriter.gsqp4a(t1, t2, n, tn)
        restart()
    # verifications
    elif is_valid_equation(t1) and is_valid_equation(t2) and is_valid_equation(tn): # given T(1), T(2) and T(n)
        t1 = eval(t1)
        t2 = eval(t2)
        tn = eval(tn)
        # calculations
        a = t1
        r = t2 / t1
        x = tn / a
        log = math.log(x, r)
        n = log + 1
        print(f"\nn = {n}\n")
        Recwriter.gsqp4b(t1, t2, tn, n)
        restart()
    else:
        print("\n*syntax error*")
        print("your lack of intelligence has resulted in errors")
        dumb_restart()

def geometric_series():
    while True:
        print("\nGeometric Series")
        # inputs
        t1 = input("Please enter your T(1): ").lower()
        if t1 == "stop":
            stop()
        elif t1 == "back":
            arithmetic_or_geometric_s()
            return
        t2 = input("Please enter your T(2): ").lower()
        if t2 == "stop":
            stop()
        elif t2 == "back":
            continue
        n = input("Please enter your n: ").lower()
        if n == "stop":
            stop()
        elif n == "back":
            continue
        tn = input("Please enter your T(n): ").lower()
        if tn == "stop":
            stop()
        elif n == "back":
            continue
        break
    # verifications
    if is_valid_equation(t1) and is_valid_equation(t2) and is_valid_equation(n): # given T(1), T(2) and n
        t1 = eval(t1)
        t2 = eval(t2)
        n = eval(n)
        # calculations
        a = t1
        r = t2 / t1
        sn = (a * (1 - (r ** n))) / (1 - r)
        print(f"\nS({n}) = {sn}\n")
        Recwriter.gsrp4a(t1, t2, n, sn)
        restart()
    # verifications
    elif is_valid_equation(t1) and is_valid_equation(t2) and is_valid_equation(tn): # given T(1), T(2) and T(n)
        t1 = eval(t1)
        t2 = eval(t2)
        tn = eval(tn)
        # calculations
        a = t1
        r = t2 / t1
        x = tn / a
        log = math.log(x, r)
        n = log + 1
        sn = (a * (1 - (r ** n))) / (1 - r)
        print(f"\nS({n}) = {sn}\n")
        Recwriter.gsrp4b(t1, t2, tn, sn)
        restart()
    else:
        print("\n*syntax error*")
        print("your lack of intelligence has resulted in errors")
        dumb_restart()

if __name__ == "__main__":
    print("Error: please execute 'start.py' to start Dumbass Calculator")
    exit()

import math
import json
from dependencies.main import stop, restart, dumb_restart
from dependencies.checks import is_valid_equation
from dependencies.lobby import probability_calculation
from dependencies.recwriter import Recwriter

def expected_value():
    exp_value_list = []
    prob_sum = []
    value_list = []
    prob_list = []
    while True:
        while True:
            print("\nExpected Value")
            print(f"Entered probability: {prob_sum}")
            # inputs
            invalue = input("Please enter the gain/loss of this event: ").lower()
            if invalue == "stop":
                stop()
            elif invalue == "back":
                probability_calculation()
                return
            inprob = input("Please enter the probability of this event: ").lower()
            if inprob == "stop":
                stop()
            elif inprob == "back":
                continue
            break
        if is_valid_equation(invalue) and is_valid_equation(inprob): # verifications
            value = eval(invalue)
            prob = eval(inprob)
            # calculations
            prob_sum.append(prob)
            exp_value_list.append(value * prob)
            if sum(prob_sum) < 1:
                value_list.append(invalue)
                prob_list.append(inprob)
                continue
            elif sum(prob_sum) == 1:
                value_list.append(invalue)
                prob_list.append(inprob)
                break
            elif sum(prob_sum) > 1:
                print("\nyou have entered a combined probability higher than 100%")
                dumb_restart()
        else:
            print("\n*syntax error*")
            print("your lack of intelligence has resulted in errors")
            dumb_restart()
    exp_value = sum(exp_value_list)
    print(f"\nValues: {value_list}")
    print(f"Probabilities: {prob_list}")
    print(f"Expected Value = {exp_value}\n")
    Recwriter.evp7a(value_list, prob_list, exp_value)
    restart()

def binomial_distribution():
    while True:
        print("\nBinomial Distribution")
        # inputs
        inn = input("Please enter the amount of trials: ").lower()
        if inn == "stop":
            stop()
        elif inn == "back":
            probability_calculation()
            return
        ins = input("Please enter (<, <=, =, >=, >) for the desired outcome: ").lower()
        if ins == "stop":
            stop()
        elif ins == "back":
            continue
        inx = input("Please enter the desired outcome: ").lower()
        if inx == "stop":
            stop()
        elif inx == "back":
            continue
        inp = input("Please enter the probability of success on a single trial: ").lower()
        if inp == "stop":
            stop()
        elif inp == "back":
            continue
        break
    # verifications
    if is_valid_equation(inn) and is_valid_equation(inx) and is_valid_equation(inp) and ins == "=":
        n = eval(inn)
        x = eval(inx)
        p = eval(inp)
        # calculations
        if n >= x:
            P = math.comb(n, x) * (p ** x) * ((1 - p) ** (n - x))
            print(f"\nP(X{ins}{inx}) = {P}\n")
            Recwriter.bdp7a(inn, ins, inx, inp, P)
            restart()
        else:
            print("\nthe desired outcome cannot be greater than the number of trials")
            dumb_restart()
    # verifications
    elif is_valid_equation(inn) and is_valid_equation(inx) and is_valid_equation(inp) and ins == ">":
        n = eval(inn)
        x = eval(inx)
        p = eval(inp)
        # calculations
        if n >= x:
            P = 0
            while n > x:
                P += math.comb(n, x) * (p ** x) * ((1 - p) ** (n - x))
                x += 1
            print(f"\nP(X{ins}{inx}) = {P}\n")
            Recwriter.bdp7a(inn, ins, inx, inp, P)
            restart()
        else:
            print("\nthe desired outcome cannot be greater than the number of trials")
            dumb_restart()
    # verifications
    elif is_valid_equation(inn) and is_valid_equation(inx) and is_valid_equation(inp) and ins == ">=":
        n = eval(inn)
        x = eval(inx)
        p = eval(inp)
        # calculations
        if n >= x:
            P = 0
            while n >= x:
                P += math.comb(n, x) * (p ** x) * ((1 - p) ** (n - x))
                x += 1
            print(f"\nP(X{ins}{inx}) = {P}\n")
            Recwriter.bdp7a(inn, ins, inx, inp, P)
            restart()
        else:
            print("\nthe desired outcome cannot be greater than the number of trials")
            dumb_restart()
    # verifications
    elif is_valid_equation(inn) and is_valid_equation(inx) and is_valid_equation(inp) and ins == "<":
        n = eval(inn)
        x = eval(inx)
        p = eval(inp)
        # calculations
        if n >= x:
            P = 0
            x -= 1
            while 0 <= x:
                P += math.comb(n, x) * (p ** x) * ((1 - p) ** (n - x))
                x -= 1
            print(f"\nP(X{ins}{inx}) = {P}\n")
            Recwriter.bdp7a(inn, ins, inx, inp, P)
            restart()
        else:
            print("\nthe desired outcome cannot be greater than the number of trials")
            dumb_restart()
    # verifications
    elif is_valid_equation(inn) and is_valid_equation(inx) and is_valid_equation(inp) and ins == "<=":
        n = eval(inn)
        x = eval(inx)
        p = eval(inp)
        # calculations
        if n >= x:
            P = 0
            while 0 <= x:
                P += math.comb(n, x) * (p ** x) * ((1 - p) ** (n - x))
                x -= 1
            print(f"\nP(X{ins}{inx}) = {P}\n")
            Recwriter.bdp7a(inn, ins, inx, inp, P)
            restart()
        else:
            print("\nthe desired outcome cannot be greater than the number of trials")
            dumb_restart()
    else:
        print("\n*syntax error*")
        print("your lack of intelligence has resulted in errors")
        dumb_restart()

def poisson_distribution():
    while True:
        print("\nPoisson Distribution")
        # inputs
        inl = input("Please enter the lambda or mean number of occurrences in the interval: ").lower()
        if inl == "stop":
            stop()
        elif inl == "back":
            probability_calculation()
            return
        ins = input("Please enter (<, <=, =, >=, >) for the number of occurrences: ").lower()
        if ins == "stop":
            stop()
        elif ins == "back":
            continue
        inx = input("Please enter the number of occurrences: ").lower()
        if inx == "stop":
            stop()
        elif inx == "back":
            continue
        break
    # verifications
    if is_valid_equation(inl) and is_valid_equation(inx) and ins == "=":
        l = eval(inl)
        x = eval(inx)
        # calculations
        P = math.exp(-l) * ((l ** x) / (math.factorial(x)))
        print(f"\nP(X{ins}{inx}) = {P}\n")
        Recwriter.pdp7a(inl, ins, inx, P)
        restart()
    # verifications
    elif is_valid_equation(inl) and is_valid_equation(inx) and ins == ">":
        l = eval(inl)
        x = eval(inx)
        # calculations
        P = 0
        while 0 <= x:
            P += math.exp(-l) * ((l ** x) / (math.factorial(x)))
            x -= 1
        P = 1 - P
        print(f"\nP(X{ins}{inx}) = {P}\n")
        Recwriter.pdp7a(inl, ins, inx, P)
        restart()
    # verifications
    elif is_valid_equation(inl) and is_valid_equation(inx) and ins == ">=":
        l = eval(inl)
        x = eval(inx)
        # calculations
        P = 0
        x -= 1
        while 0 <= x:
            P += math.exp(-l) * ((l ** x) / (math.factorial(x)))
            x -= 1
        P = 1 - P
        print(f"\nP(X{ins}{inx}) = {P}\n")
        Recwriter.pdp7a(inl, ins, inx, P)
        restart()
    # verifications
    elif is_valid_equation(inl) and is_valid_equation(inx) and ins == "<":
        l = eval(inl)
        x = eval(inx)
        # calculations
        P = 0
        x -= 1
        while 0 <= x:
            P += math.exp(-l) * ((l ** x) / (math.factorial(x)))
            x -= 1
        print(f"\nP(X{ins}{inx}) = {P}\n")
        Recwriter.pdp7a(inl, ins, inx, P)
        restart()
    # verifications
    elif is_valid_equation(inl) and is_valid_equation(inx) and ins == "<=":
        l = eval(inl)
        x = eval(inx)
        # calculations
        P = 0
        while 0 <= x:
            P += math.exp(-l) * ((l ** x) / (math.factorial(x)))
            x -= 1
        print(f"\nP(X{ins}{inx}) = {P}\n")
        Recwriter.pdp7a(inl, ins, inx, P)
        restart()
    else:
        print("\n*syntax error*")
        print("your lack of intelligence has resulted in errors")
        dumb_restart()

def normal_distribution():
    while True:
        print("\nNormal Distribution")
        # inputs
        innx = input("Please enter the number < X: ").lower()
        if innx == "stop":
            stop()
        elif innx == "back":
            probability_calculation()
            return
        inxn = input("Please enter the number > X: ").lower()
        if inxn == "stop":
            stop()
        elif inxn == "back":
            continue
        inm = input("Please enter the mean of distribution: ").lower()
        if inm == "stop":
            stop()
        elif inm == "back":
            continue
        ins = input("Please enter the standard deviation of distribution: ").lower()
        if ins == "stop":
            stop()
        elif ins == "back":
            continue
        break
    # verifications
    if is_valid_equation(innx) and is_valid_equation(inxn) and is_valid_equation(inm) and is_valid_equation(ins):
        nx = eval(innx)
        xn = eval(inxn)
        m = eval(inm)
        s = eval(ins)
        with open("dependencies/z_score_table.json", "r") as f:
            z_table = json.load(f)
        # calculations
        zn = (xn - m) / s
        nz = (nx - m) / s
        if nz == 0:
            ans = z_table[f"{zn:.2f}"]
        elif zn == 0:
            ans = z_table[f"{-nz:.2f}"]
        else:
            ans = z_table[f"{zn:.2f}"] + z_table[f"{-nz:.2f}"]
        print(f"\nP({innx}<X<{inxn}) = {ans}\n")
        Recwriter.ndp7c(innx, inxn, inm, ins, ans)
        restart()
    # verifications
    elif is_valid_equation(innx) and is_valid_equation(inm) and is_valid_equation(ins):
        nx = eval(innx)
        m = eval(inm)
        s = eval(ins)
        with open("dependencies/z_score_table.json", "r") as f:
            z_table = json.load(f)
        # calculations
        zn = (nx - m) / s
        if zn >= 0:
            ans = 0.5 - z_table[f"{zn:.2f}"]
        elif zn < 0:
            zn = -zn
            ans = 0.5 + z_table[f"{zn:.2f}"]
        print(f"\nP(X>{innx}) = {ans}\n")
        Recwriter.ndp7a(innx, inm, ins, ans)
        restart()
    # verifications
    elif is_valid_equation(inxn) and is_valid_equation(inm) and is_valid_equation(ins):
        xn = eval(inxn)
        m = eval(inm)
        s = eval(ins)
        with open("dependencies/z_score_table.json", "r") as f:
            z_table = json.load(f)
        # calculations
        zn = (xn - m) / s
        if zn >= 0:
            ans = 0.5 + z_table[f"{zn:.2f}"]
        elif zn < 0:
            zn = -zn
            ans = 0.5 - z_table[f"{zn:.2f}"]
        print(f"\nP(X<{inxn}) = {ans}\n")
        Recwriter.ndp7b(inxn, inm, ins, ans)
        restart()
    else:
        print("\n*syntax error*")
        print("your lack of intelligence has resulted in errors")
        dumb_restart()
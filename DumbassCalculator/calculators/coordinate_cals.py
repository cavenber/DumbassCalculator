import math
from dependencies.main import stop, restart, dumb_restart
from dependencies.checks import is_valid_equation
from dependencies.lobby import coordinate_geometry
from dependencies.recwriter import Recwriter

def midpoint_formula():
    while True:
        print("\nMid-Point Formula")
        # inputs
        a = input("Please enter your A(x,y): ").lower()
        if a == "stop":
            stop()
        elif a == "back":
            coordinate_geometry()
            return
        b = input("Please enter your B(x,y): ").lower()
        if b == "stop":
            stop()
        elif b == "back":
            continue
        break
    # verifications
    if is_valid_equation(a) and is_valid_equation(b):
        a = eval(a)
        b = eval(b)
        # calculations
        m = [(a[0] + b[0]) / 2, (a[1] + b[1]) / 2]
        print(f"\nM = {m}\n")
        Recwriter.mfp5a(a, b, m)
        restart()
    else:
        print("\n*syntax error*")
        print("your lack of intelligence has resulted in errors")
        dumb_restart()

def line_slope():
    while True:
        print("\nLine Slope")
        # inputs
        a = input("Please enter your A(x,y): ").lower()
        if a == "stop":
            stop()
        elif a == "back":
            coordinate_geometry()
            return
        b = input("Please enter your B(x,y): ").lower()
        if b == "stop":
            stop()
        elif b == "back":
            continue
        break
    # verifications
    if is_valid_equation(a) and is_valid_equation(b):
        a = eval(a)
        b = eval(b)
        # calculations
        try:
            m = (b[1] - a[1]) / (b[0] - a[0])
            print(f"\nm = {m}\n")
            Recwriter.lsp5a(a, b, m)
        except ZeroDivisionError:
            print("m = undefined")
            Recwriter.lsp5b(a, b)
        restart()
    else:
        print("\n*syntax error*")
        print("your lack of intelligence has resulted in errors")
        dumb_restart()

def line_equation():
    while True:
        print("\nLine Equation")
        # inputs
        a = input("Please enter your A(x,y): ").lower()
        if a == "stop":
            stop()
        elif a == "back":
            coordinate_geometry()
            return
        b = input("Please enter your B(x,y): ").lower()
        if b == "stop":
            stop()
        elif b == "back":
            continue
        break
    # verifications
    if is_valid_equation(a) and is_valid_equation(b):
        a = eval(a)
        b = eval(b)
        # calculations
        try:
            m = (b[1] - a[1]) / (b[0] - a[0])
            c = a[1] - (m * a[0])
            if c < 0:
                cs = "-"
                cx = -c
            else:
                cs = "+"
                cx = c
            print(f"\ny = {m}x {cs} {cx}\n")
            use = input("Would you like to use this equation? (y/n): ").lower()
            if use == "y":
                while True:
                    x = input("Please enter your x: ").lower()
                    if x == "stop":
                        Recwriter.lep5a(a, b, m, cs,cx)
                        stop()
                    elif x == "back":
                        line_equation()
                        return
                    y = input("Please enter your y: ").lower()
                    if y == "stop":
                        stop()
                    elif y == "back":
                        continue
                    break
                if is_valid_equation(x):
                    x = eval(x)
                    y = m * x + c
                    print(f"\ny = {y}\n")
                    Recwriter.lep5b(a, b, m, cs, cx, x, y)
                    restart()
                elif is_valid_equation(y):
                    y = eval(y)
                    x = (y - c) / m
                    print(f"\nx = {x}\n")
                    Recwriter.lep5c(a, b, m, cs, cx, y, x)
                    restart()
                else:
                    print("\n*syntax error*")
                    print("your lack of intelligence has resulted in errors")
                    dumb_restart()
            elif use == "n":
                Recwriter.lep5a(a, b, m, cs, cx)
                restart()
            else:
                print("\n*syntax error*")
                print("the function you selected does not exist, please check your intelligence and try again")
                dumb_restart()
        except ZeroDivisionError:
            print(f"\nMath error due to m = Undefined\n")
            Recwriter.lep5d(a, b)
            restart()
    else:
        print("\n*syntax error*")
        print("your lack of intelligence has resulted in errors")
        dumb_restart()

def distance_formula():
    while True:
        print("\nDistance Formula")
        # inputs
        a = input("Please enter your A(x,y): ").lower()
        if a == "stop":
            stop()
        elif a == "back":
            coordinate_geometry()
            return
        b = input("Please enter your B(x,y): ").lower()
        if b == "stop":
            stop()
        elif b == "back":
            continue
        break
    # verifications
    if is_valid_equation(a) and is_valid_equation(b):
        a = eval(a)
        b = eval(b)
        # calculations
        d = (((b[0] - a[0]) ** 2) + ((b[1] - a[1]) ** 2)) ** 0.5
        print(f"\nDistance between the two points = {d}\n")
        Recwriter.dfp5a(a, b, d)
        restart()
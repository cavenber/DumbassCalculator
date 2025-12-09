
if __name__ == "__main__":
    print("Error: please execute 'start.py' to start Dumbass Calculator")
    exit()

import math
from dependencies.main import start, stop, restart, dumb_restart
from dependencies.checks import is_valid_int, is_valid_expression, is_valid_equation, replacer
from dependencies.recwriter import Recwriter

def arithmetic_operation():
    print("\nArithmetic Operation")
    # inputs
    equationIn = input("Please enter your calculation ('help' for assistance): ").lower()
    if equationIn == "stop":
        stop()
    elif equationIn == "back":
        start()
        return
    elif equationIn == "help":
        print("\nEnter any calculation within syntax:\n"
            "+ = Addition\n"
            "- = Subtraction\n"
            "* = Multiplication\n"
            "/ = Division\n"
            "** = Exponentiation\n"
            "() can be used\n"
            "sqrt(), radians(), sin(), cos(), tan(), log() can be used")
        arithmetic_operation()
    elif equationIn in ["2 + 2", "2+2", "2 +2", "2+ 2"]: # Radiohead reference
        ans = 5
        print(f"\nResult of the entered calculation is {ans} due to the Radiohead song '2 + 2 = 5'\n")
        Recwriter.p1a("2 + 2", ans)
        restart()
    # verifications
    equationIn = replacer(equationIn)
    if is_valid_equation(equationIn):
        equation = equationIn
        math_functions = ['sqrt', 'radians', 'sin', 'cos', 'tan', 'log']
        for func in math_functions:
            equation = equation.replace(func, f'math.{func}')
        # calculations
        ans = eval(equation, {"__builtins__": {}, "math": math})
        print(f"\nResult of the entered calculation is {ans}\n")
        Recwriter.p1a(equationIn, ans)
        restart()
    else:
        print("\n*syntax error*")
        print("your lack of intelligence has resulted in errors")
        dumb_restart()

def quadratic_equation():
    while True:
        print("\nQuadratic Equation")
        # inputs
        a = input("Please enter your a: ").lower()
        if a == "stop":
            stop()
        elif a == "back":
            start()
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
    a = replacer(a)
    b = replacer(b)
    c = replacer(c)
    # verifications
    if is_valid_expression(a) and is_valid_expression(b) and is_valid_expression(c):
        a = eval(a)
        b = eval(b)
        c = eval(c)
        if a == 0:
            print("\n*zero division error*")
            print("your lack of intelligence has resulted in errors")
            dumb_restart()
            return
        # calculations
        discriminant = (b ** 2) - (4 * a * c)
        if discriminant < 0:
            print("\nThere are no real roots\n")
            Recwriter.p2c(a, b, c)
            restart()
        elif discriminant == 0:
            x = (-b + ((b ** 2) - 4 * (a * c)) ** 0.5) / (2 * a)
            if x < 0:
                xs = "+"
                xx = -x
            else:
                xs = "-"
                xx = x
            print(f"\n(x {xs} {xx}) ** 2 = 0\n"
                  f"x = {x}\n")
            Recwriter.p2b(a, b, c, x)
            restart()
        elif discriminant > 0:
            x1 = (-b + ((b ** 2) - 4 * (a * c)) ** 0.5) / (2 * a)
            x2 = (-b - ((b ** 2) - 4 * (a * c)) ** 0.5) / (2 * a)
            if x1 < 0:
                x1s = "+"
                x1x = -x1
            else:
                x1s = "-"
                x1x = x1
            if x2 < 0:
                x2s = "+"
                x2x = -x2
            else:
                x2s = "-"
                x2x = x2
            print(f"\n(x {x1s} {x1x}) (x {x2s} {x2x}) = 0\n"
                  f"x = {x1} or x = {x2}\n")
            Recwriter.p2a(a, b, c, x1, x2)
            restart()
    else:
        print("\n*syntax error*")
        print("your lack of intelligence has resulted in errors")
        dumb_restart()

def set_operation():
    while True:
        print("\nSet Operation")
        # input
        a = input("Please enter your list A: ").lower()
        if a == "stop":
            stop()
        elif a == "back":
            start()
            return
        op = input("Please enter your operation (u: union, i: intersection, d: difference ): ").lower()
        if op == "stop":
            stop()
        elif op == "back":
            continue
        b = input("Please enter your list B: ").lower()
        if b == "stop":
            stop()
        elif b == "back":
            continue
        break
    a = replacer(a)
    b = replacer(b)
    # verification
    if is_valid_expression(a) and is_valid_expression(b) and op in ("u", "i", "d"): # verification
        a = eval(a)
        b = eval(b)
        if op == "u": # calculation
            ans = list(set(a).union(b))
            print(f"\nThe union of A and B is {ans}\n")
            Recwriter.p8a(a, b, ans)
            restart()
        elif op == "i":
            ans = list(set(a).intersection(b))
            print(f"\nThe intersection of A and B is {ans}\n")
            Recwriter.p8b(a, b, ans)
            restart()
        elif op == "d":
            ans = list(set(a).difference(b))
            print(f"\nThe difference of A and B is {ans}\n")
            Recwriter.p8c(a, b, ans)
            restart()
    else:
        print("\n*syntax error*")
        print("your lack of intelligence has resulted in errors")
        dumb_restart()

def dec_bin_conversion():
    while True:
        print("\nDecimal & Binary Conversion")
        # input
        dorb = input("Please choose your type of number (d: decimal, b: binary): ").lower()
        if dorb == "stop":
            stop()
        elif dorb == "back":
            start()
            return
        num = input("Please enter your number: ").lower()
        if num == "stop":
            stop()
        elif num == "back":
            continue
        break
    num = replacer(num)
    if dorb == "b":
        if is_valid_expression(num): # verification
            num = eval(num)
            ans = []
            if type(num) == tuple:
                d, p = 0, 0
                for b in num: # calculation
                    d, p = 0, 0
                    while b:
                        d += (b % 10) * (2 ** p)
                        b //= 10
                        p += 1
                    ans.append(d)
            else:
                d, p = 0, 0
                b = num
                while b: # calculation
                    d += (b % 10) * (2 ** p)
                    b //= 10
                    p += 1
                ans.append(d)
            print(f"\nThe binary to decimal conversion result is {ans}\n")
            Recwriter.p9a(num, ans)
            restart()
        else:
            print("\n*syntax error*")
            print("your lack of intelligence has resulted in errors")
            dumb_restart()
    elif dorb == "d":
        if is_valid_expression(num): # verification
            num = eval(num)
            ans = []
            if type(num) == tuple:
                for n in num: # calculation
                    b = ""
                    while n > 0:
                        b = str(n % 2) + b
                        n //= 2
                    ans.append(b)
            else:
                b = ""
                n = num
                while n > 0: # calculation
                    b = str(n % 2) + b
                    n //= 2
                ans.append(b)
            print(f"\nThe decimal to binary conversion result is {ans}\n")
            Recwriter.p9b(num, ans)
            restart()
        else:
            print("\n*syntax error*")
            print("your lack of intelligence has resulted in errors")
            dumb_restart()
    else:
        print("\n*syntax error*")
        print("your lack of intelligence has resulted in errors")
        dumb_restart()

def caesar_cipher_encoder():
    while True:
        print("\nCaesar Cipher Encoder")
        # input
        textIn = input("Please enter your text: ").lower()
        if textIn == "stop":
            stop()
        elif textIn == "back":
            start()
            return
        shift = input("Please enter the amount of shifts: ").lower()
        if shift == "stop":
            stop()
        elif shift == "back":
            continue
        break
    textIn = replacer(textIn)
    shift = replacer(shift)
    if is_valid_int(shift):
        shift = int(shift)
        text = list(textIn)
        temp = []
        for i in text:
            if i == ' ':
                temp.append(i)
            else:
                p = ord(i) - 97
                temp.append(chr(((p + shift) % 26) + 97))
        cipher = "".join(temp)
        print(f"\nThe coded message is '{cipher}'\n")
        Recwriter.p10a(textIn, shift, cipher)
        restart()
    else:
        print("\n*syntax error*")
        print("your lack of intelligence has resulted in errors")
        dumb_restart()

if __name__ == "__main__":
    print("Error: please execute 'start.py' to start Dumbass Calculator")
    exit()

import json
from dependencies.main import stop, restart, dumb_restart
from dependencies.checks import is_valid_expression, replacer
from dependencies.lobby import variation, joint_variation
from dependencies.recwriter import Recwriter

def direct_variation():
    with open("dependencies/data.json", "r") as f:
        data = json.load(f)
    while True:
        print("\nDirect Variation")
        # inputs
        x = input("Please enter your x: ").lower()
        if x == "stop":
            stop()
        elif x == "back":
            variation()
            return
        y = input("Please enter your y: ").lower()
        if y == "stop":
            stop()
        elif y == "back":
            continue
        break
    x = replacer(x)
    y = replacer(y)
    # verifications
    if is_valid_expression(x) and is_valid_expression(y):
        x = eval(x)
        y = eval(y)
        # calculations
        k = y / x
        print(f"\ny = {k} * x\n")
        data["ans"] = str(k)
        with open("dependencies/data.json", "w") as f:
            json.dump(data, f)
        # use the calculated equation
        use = input("Would you like to use this equation? (y/n): ").lower()
        if use == "y":
            with open("dependencies/data.json", "r") as f:
                data = json.load(f)
            while True:
                # inputs
                x = input("Please enter your x: ").lower()
                if x == "stop":
                    Recwriter.dvp3a(k)
                    stop()
                elif x == "back":
                    direct_variation()
                    return
                y = input("Please enter your y: ").lower()
                if y == "stop":
                    Recwriter.dvp3a(k)
                    stop()
                elif y == "back":
                    continue
                break
            x = replacer(x)
            y = replacer(y)
            # verifications
            if is_valid_expression(x):
                x = eval(x)
                # calculations
                y = k * x
                print(f"\ny = {y}\n")
                data["ans"] = str(y)
                with open("dependencies/data.json", "w") as f:
                    json.dump(data, f)
                Recwriter.dvp3b(y, k, x)
                restart()
            elif is_valid_expression(y):
                y = eval(y)
                # calculations
                x = y / k
                print(f"\nx = {x}\n")
                data["ans"] = str(x)
                with open("dependencies/data.json", "w") as f:
                    json.dump(data, f)
                Recwriter.dvp3b(y, k, x)
                restart()
            else:
                print("\n*syntax error*")
                print("your lack of intelligence has resulted in errors")
                dumb_restart()
        elif use == "n":
            Recwriter.dvp3a(k)
            restart()
        else:
            print("\n*syntax error*")
            print("the function you selected does not exist, please check your intelligence and try again")
            dumb_restart()
    else:
        print("\n*syntax error*")
        print("your lack of intelligence has resulted in errors")
        dumb_restart()

def inverse_variation():
    with open("dependencies/data.json", "r") as f:
        data = json.load(f)
    while True:
        print("\nInverse Variation")
        # inputs
        x = input("Please enter your x: ").lower()
        if x == "stop":
            stop()
        elif x == "back":
            variation()
            return
        y = input("Please enter your y: ").lower()
        if y == "stop":
            stop()
        elif y == "back":
            continue
        break
    x = replacer(x)
    y = replacer(y)
    # verifications
    if is_valid_expression(x) and is_valid_expression(y):
        x = eval(x)
        y = eval(y)
        # calculations
        k = y * x
        print(f"\ny = {k} / x\n")
        data["ans"] = str(k)
        with open("dependencies/data.json", "w") as f:
            json.dump(data, f)
        # use the calculated equation
        use = input("Would you like to use this equation? (y/n): ").lower()
        if use == "y":
            with open("dependencies/data.json", "r") as f:
                data = json.load(f)
            while True:
                # inputs
                x = input("Please enter your x: ").lower()
                if x == "stop":
                    Recwriter.ivp3a(k)
                    stop()
                elif x == "back":
                    inverse_variation()
                    return
                y = input("Please enter your y: ").lower()
                if y == "stop":
                    Recwriter.ivp3a(k)
                    stop()
                elif y == "back":
                    continue
                break
            x = replacer(x)
            y = replacer(y)
            #verifications
            if is_valid_expression(x):
                x = eval(x)
                # calculations
                y = k / x
                print(f"\ny = {y}\n")
                data["ans"] = str(y)
                with open("dependencies/data.json", "w") as f:
                    json.dump(data, f)
                Recwriter.ivp3b(y, k, x)
                restart()
            elif is_valid_expression(y):
                y = eval(y)
                # calculations
                x = k / y
                print(f"\nx = {x}\n")
                data["ans"] = str(x)
                with open("dependencies/data.json", "w") as f:
                    json.dump(data, f)
                Recwriter.ivp3b(y, k, x)
            else:
                print("\n*syntax error*")
                print("your lack of intelligence has resulted in errors")
                dumb_restart()
        elif use == "n":
            Recwriter.ivp3a(k)
            restart()
        else:
            print("\n*syntax error*")
            print("the function you selected does not exist, please check your intelligence and try again")
            dumb_restart()
    else:
        print("\n*syntax error*")
        print("your lack of intelligence has resulted in errors")
        dumb_restart()

def joint_variation_form1():
    with open("dependencies/data.json", "r") as f:
        data = json.load(f)
    while True:
        print("\nJoint Variation")
        print("According to z = k * x * y")
        # inputs
        x = input("Please enter your x: ").lower()
        if x == "stop":
            stop()
        elif x == "back":
            joint_variation()
            return
        y = input("Please enter your y: ").lower()
        if y == "stop":
            stop()
        elif y == "back":
            continue
        z = input("Please enter your z: ").lower()
        if z == "stop":
            stop()
        elif z == "back":
            continue
        break
    x = replacer(x)
    y = replacer(y)
    z = replacer(z)
    # verifications
    if is_valid_expression(x) and is_valid_expression(y) and is_valid_expression(z):
        x = eval(x)
        y = eval(y)
        z = eval(z)
        # calculations
        k = x * y
        k = z / k
        print(f"\nz = {k} * x * y\n")
        data["ans"] = str(k)
        with open("dependencies/data.json", "w") as f:
            json.dump(data, f)
        # use the calculated equation
        use = input("Would you like to use this equation? (y/n) ").lower()
        if use == "y":
            with open("dependencies/data.json", "r") as f:
                data = json.load(f)
            while True:
                # inputs
                x = input("Please enter your x: ").lower()
                if x == "stop":
                    Recwriter.jv1p3a(k)
                    stop()
                elif x == "back":
                    joint_variation_form1()
                    return
                y = input("Please enter your y: ").lower()
                if y == "stop":
                    Recwriter.jv1p3a(k)
                    stop()
                elif y == "back":
                    continue
                break
            x = replacer(x)
            y = replacer(y)
            # verifications
            if is_valid_expression(x) and is_valid_expression(y):
                x = eval(x)
                y = eval(y)
                # calculations
                z = k * x * y
                print(f"\nz = {z}\n")
                data["ans"] = str(z)
                with open("dependencies/data.json", "w") as f:
                    json.dump(data, f)
                Recwriter.jv1p3b(z, k, x, y)
                restart()
            else:
                print("\n*syntax error*")
                print("your lack of intelligence has resulted in errors")
                dumb_restart()
        elif use == "n":
            Recwriter.jv1p3a(k)
            restart()
        else:
            print("\n*syntax error*")
            print("the function you selected does not exist, please check your intelligence and try again")
            dumb_restart()
    else:
        print("\n\n*syntax error*")
        print("your lack of intelligence has resulted in errors")
        dumb_restart()

def joint_variation_form2():
    with open("dependencies/data.json", "r") as f:
        data = json.load(f)
    while True:
        print("\nJoint Variation")
        print("According to z = k * x / y")
        # inputs
        x = input("Please enter your x: ").lower()
        if x == "stop":
            stop()
        elif x == "back":
            joint_variation()
            return
        y = input("Please enter your y: ").lower()
        if y == "stop":
            stop()
        elif y == "back":
            continue
        z = input("Please enter your z: ").lower()
        if z == "stop":
            stop()
        elif z == "back":
            continue
        break
    x = replacer(x)
    y = replacer(y)
    z = replacer(z)
    # verifications
    if is_valid_expression(x) and is_valid_expression(y) and is_valid_expression(z):
        x = eval(x)
        y = eval(y)
        z = eval(z)
        # calculations
        e = z * y
        k = e / x
        print(f"\nz = {k} * x / y\n")
        data["ans"] = str(k)
        with open("dependencies/data.json", "w") as f:
            json.dump(data, f)
        # use the calculated equation
        use = input("Would you like to use this equation? (y/n): ").lower()
        if use == "y":
            with open("dependencies/data.json", "r") as f:
                data = json.load(f)
            while True:
                # inputs
                x = input("Please enter your x: ").lower()
                if x == "stop":
                    Recwriter.jv2p3a(k)
                    stop()
                elif x == "back":
                    joint_variation_form2()
                    return
                y = input("Please enter your y: ").lower()
                if y == "stop":
                    Recwriter.jv2p3a(k)
                    stop()
                elif y == "back":
                    continue
                break
            x = replacer(x)
            y = replacer(y)
            # verifications
            if is_valid_expression(x) and is_valid_expression(y):
                x = eval(x)
                y = eval(y)
                # calculations
                z = k * x / y
                print(f"\nz = {z}\n")
                data["ans"] = str(z)
                with open("dependencies/data.json", "w") as f:
                    json.dump(data, f)
                Recwriter.jv2p3b(z, k, x, y)
                restart()
            else:
                print("\n\n*syntax error*")
                print("your lack of intelligence has resulted in errors")
                dumb_restart()
        elif use == "n":
            Recwriter.jv2p3b(z, k, x, y)
            restart()
        else:
            print("\n\n*syntax error*")
            print("the function you selected does not exist, please check your intelligence and try again")
            dumb_restart()
    else:
        print("\n\n*syntax error*")
        print("your lack of intelligence has resulted in errors")
        dumb_restart()

###### CHECKS ######

if __name__ == "__main__":
    print("Error: please execute 'start.py' to start Dumbass Calculator")
    exit()

# to verify if the input number is a valid float
def is_valid_int(ss):
    try:
        int(ss)
        return True
    except ValueError:
        return False

def is_valid_expression(ss):
    pattern = r"^[\d\s+\-*/%(),.]+\**$"
    if re.match(pattern, ss):
        try:
            eval(ss, {"__builtins__": {}, "math": math})
            return True
        except (ZeroDivisionError, SyntaxError, ValueError, TypeError, AttributeError):
            return False
    else:
        return False

# to verify if the input string is a valid equation
def is_valid_equation(ss):
    pattern = r'^[\d\s+\-*/%(),.]*(?:\b(sqrt|radians|sin|cos|tan|log)\s*\([^)]*\)\s*)*[\d\s+\-*/%(),.]*$'
    if re.match(pattern, ss):
        math_functions = ['sqrt', 'radians', 'sin', 'cos', 'tan', 'log']
        for func in math_functions:
            ss = ss.replace(func, f'math.{func}')
        try:
            eval(ss, {"__builtins__": {}, "math": math})
            return True
        except (ZeroDivisionError, SyntaxError, ValueError, TypeError, AttributeError):
            return False
    else:
        return False

def replacer(user_input):
    with open("dependencies/data.json") as f:
        data = json.load(f)
    if "(ans)" in user_input:
        user_input = user_input.replace("ans", data["ans"])
    if "(x1)" in user_input:
        user_input = user_input.replace("x1", data["x1"])
    if "(x2)" in user_input:
        user_input = user_input.replace("x2", data["x2"])
    return user_input

import re
import math
import json
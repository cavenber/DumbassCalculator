
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

import re
import math
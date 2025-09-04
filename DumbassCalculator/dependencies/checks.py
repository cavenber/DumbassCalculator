
###### CHECKS ######

# to verify if the input number is a valid float
def is_valid_number(ss):
    try:
        float(ss)
        return True
    except ValueError:
        return False

# to verify if the input string is a valid equation
def is_valid_equation(ss):
    pattern = r"^[\d\s+\-*/(),.]+$"
    if re.match(pattern, ss):
        try:
            eval(ss)
            return True
        except (ZeroDivisionError, SyntaxError, ValueError, TypeError):
            return False
    else:
        return False

import re
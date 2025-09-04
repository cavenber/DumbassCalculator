
###### LOBBIES ######

# choose a type of variation
def variation():
    print("\nVariation Calculations\n"
        "1: Direct Variation\n"
        "2: Inverse Variation\n"
        "3: Joint Variation")
    # inputs
    prog = input("Please choose a type of variation (1-3): ").lower()
    if prog == "stop":
        stop()
    elif prog == "back":
        start()
        return
    # portals
    elif prog == "1":
        direct_variation()
    elif prog == "2":
        inverse_variation()
    elif prog == "3":
        joint_variation()
    else:
        print("the program you selected does not exist, please check your intelligence and try again")
        dumb_restart()

# choose between the 2 types of joint variations
def joint_variation():
    # inputs
    print("\nJoint Variation\n"
        "1: z = k * x * y\n"
        "2: z = k * x / y")
    prog = input("Please choose between the two forms of joint variation (1-2): ").lower()
    if prog == "stop":
        stop()
    elif prog == "back":
        start()
        return
    # portals
    elif prog == "1":
        joint_variation_form1()
    elif prog == "2":
        joint_variation_form2()
    else:
        print("the program you selected does not exist, please check your intelligence and try again")
        dumb_restart()

# lobby for arithmetic or geometric sequence or series
def arithmetic_or_geometric_s():
    # inputs
    print("\nArithmetic Sequence/Series & Geometric Sequence/Series Calculations\n"
        "1: Arithmetic Sequence\n"
        "2: Arithmetic Series\n"
        "3: Geometric Sequence\n"
        "4: Geometric Series")
    prog = input("Please choose the calculation you desire (1-4): ").lower()
    if prog == "stop":
        stop()
    elif prog == "back":
        start()
        return
    # portals
    elif prog == "1":
        arithmetic_sequence()
    elif prog == "2":
        arithmetic_series()
    elif prog == "3":
        geometric_sequence()
    elif prog == "4":
        geometric_series()
    else:
        print("the program you selected does not exist, please check your intelligence and try again")
        dumb_restart()

# lobby for coordinate geometry
def coordinate_geometry():
    # inputs
    print("\nCoordinate Geometry Calculations\n"
        "1: Mid-Point\n"
        "2: Line Slope\n"
        "3: Line Equation\n"
        "4: Distance Formula")
    prog = input("Please choose the calculation you desire (1-3): ").lower()
    if prog == "stop":
        stop()
    elif prog == "back":
        start()
        return
    # portals
    elif prog == "1":
        midpoint_formula()
    elif prog == "2":
        line_slope()
    elif prog == "3":
        line_equation()
    elif prog == "4":
        distance_formula()
    else:
        print("the program you selected does not exist, please check your intelligence and try again")
        dumb_restart()

def triangular_calculation():
    # inputs
    print("\nTriangular Calculations\n"
          "1: Pythagorean Theorem\n"
          "2: Sine Formula\n"
          "3: Cosine Formula")
    prog = input("Please choose the calculation you desire (1-3): ").lower()
    if prog == "stop":
        stop()
    elif prog == "back":
        start()
        return
    # portals
    elif prog == "1":
        pythagorean_theorem()
    elif prog == "2":
        sine_formula()
    elif prog == "3":
        cosine_formula()
    else:
        print("the program you selected does not exist, please check your intelligence and try again")
        dumb_restart()

def probability_calculation():
    print("\nProbability Calculations\n"
          "1: Expected Value\n"
          "2: Binomial Distribution\n"
          "3: Poisson Distribution\n"
          "4: Normal Distribution")
    prog = input("Please choose the calculation you desire (1-4): ").lower()
    if prog == "stop":
        stop()
    elif prog == "back":
        start()
        return
    # portals
    elif prog == "1":
        expected_value()
    elif prog == "2":
        binomial_distribution()
    elif prog == "3":
        poisson_distribution()
    elif prog == "4":
        normal_distribution()
    else:
        print("the program you selected does not exist, please check your intelligence and try again")
        dumb_restart()

from .main import start, stop, restart, dumb_restart
from calculators.variation_cals import direct_variation, inverse_variation, joint_variation_form1, joint_variation_form2
from calculators.arithgeoseqser_cals import arithmetic_sequence, arithmetic_series, geometric_sequence, geometric_series
from calculators.coordinate_cals import midpoint_formula, line_slope, line_equation, distance_formula
from calculators.triangular_cals import pythagorean_theorem, sine_formula, cosine_formula
from calculators.probability_cals import expected_value, binomial_distribution, poisson_distribution, normal_distribution
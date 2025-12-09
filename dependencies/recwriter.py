
###### RECORD WRITER ######

if __name__ == "__main__":
    print("Error: please execute 'start.py' to start Dumbass Calculator")
    exit()

class Recwriter:
    # Arithmatic Operation (p1)
    def p1a(equation, ans):
        with open("dependencies/data.json", "r") as f:
            data = json.load(f)
        data["ans"] = str(ans)
        with open("dependencies/data.json", "w") as f:
            json.dump(data, f)
        with open("dependencies/records.txt", "a") as f:
            f.write(f"\nArithmatic Operation (p1): {equation} = {ans}\n")
    # Quadratic Equation (p2)
    def p2a(a, b, c, x1, x2):
        with open("dependencies/data.json", "r") as f:
            data = json.load(f)
        data["x1"] = str(x1)
        data["x2"] = str(x2)
        with open("dependencies/data.json", "w") as f:
            json.dump(data, f)
        with open("dependencies/records.txt", "a") as f:
            f.write(f"\nQuadratic Equation (p2): a = {a}, b = {b}, c = {c}; x = {x1} or x = {x2}\n")
    def p2b(a, b, c, x):
        with open("dependencies/data.json", "r") as f:
            data = json.load(f)
        data["ans"] = str(x)
        data["x1"] = str(x)
        data["x2"] = str(x)
        with open("dependencies/data.json", "w") as f:
            json.dump(data, f)
        with open("dependencies/records.txt", "a") as f:
            f.write(f"\nQuadratic Equation (p2): a = {a}, b = {b}, c = {c}; x = {x}\n")
    def p2c(a, b, c):
        with open("dependencies/data.json", "r") as f:
            data = json.load(f)
        data["ans"] = "0"
        data["x1"] = "0"
        data["x2"] = "0"
        with open("dependencies/data.json", "w") as f:
            json.dump(data, f)
        with open("dependencies/records.txt", "a") as f:
            f.write(f"\nQuadratic Equation (p2): a = {a}, b = {b}, c = {c}; No real roots\n")
    # Direct Variation (p3)
    def dvp3a(k):
        with open("dependencies/data.json", "r") as f:
            data = json.load(f)
        data["ans"] = str(k)
        with open("dependencies/data.json", "w") as f:
            json.dump(data, f)
        with open("dependencies/records.txt", "a") as f:
            f.write(f"\nDirect Variation (p3): y = {k} * x\n")
    def dvp3b(y, k, x):
        with open("dependencies/data.json", "r") as f:
            data = json.load(f)
        data["ans"] = str(y)
        with open("dependencies/data.json", "w") as f:
            json.dump(data, f)
        with open("dependencies/records.txt", "a") as f:
            f.write(f"\nDirect Variation (p3): {y} = {k} * {x}\n")
    # Inverse Variation (p3)
    def ivp3a(k):
        with open("dependencies/data.json", "r") as f:
            data = json.load(f)
        data["ans"] = str(k)
        with open("dependencies/data.json", "w") as f:
            json.dump(data, f)
        with open("dependencies/records.txt", "a") as f:
            f.write(f"\nInverse Variation (p3): y = {k} / x\n")
    def ivp3b(y, k, x):
        with open("dependencies/data.json", "r") as f:
            data = json.load(f)
        data["ans"] = str(y)
        with open("dependencies/data.json", "w") as f:
            json.dump(data, f)
        with open("dependencies/records.txt", "a") as f:
            f.write(f"\nInverse Variation (p3): {y} = {k} / {x}\n")
    # Joint Variation Form 1 (p3)
    def jv1p3a(k):
        with open("dependencies/data.json", "r") as f:
            data = json.load(f)
        data["ans"] = str(k)
        with open("dependencies/data.json", "w") as f:
            json.dump(data, f)
        with open("dependencies/records.txt", "a") as f:
            f.write(f"\nJoint Variation (p3): z = {k} * x * y\n")
    def jv1p3b(z, k, x, y):
        with open("dependencies/data.json", "r") as f:
            data = json.load(f)
        data["ans"] = str(z)
        with open("dependencies/data.json", "w") as f:
            json.dump(data, f)
        with open("dependencies/records.txt", "a") as f:
            f.write(f"\nJoint Variation (p3): {z} = {k} * {x} * {y}\n")
    # Joint Variation Form 2 (p3)
    def jv2p3a(k):
        with open("dependencies/data.json", "r") as f:
            data = json.load(f)
        data["ans"] = str(k)
        with open("dependencies/data.json", "w") as f:
            json.dump(data, f)
        with open("dependencies/records.txt", "a") as f:
            f.write(f"\nJoint Variation (p3): z = {k} * x / y\n")
    def jv2p3b(z, k, x, y):
        with open("dependencies/data.json", "r") as f:
            data = json.load(f)
        data["ans"] = str(z)
        with open("dependencies/data.json", "w") as f:
            json.dump(data, f)
        with open("dependencies/records.txt", "a") as f:
            f.write(f"\nJoint Variation (p3): {z} = {k} * {x} / {y}\n")
    # Arithmetic Sequence (p4)
    def asqp4a(t1, t2, n, tn):
        with open("dependencies/data.json", "r") as f:
            data = json.load(f)
        data["ans"] = str(tn)
        with open("dependencies/data.json", "w") as f:
            json.dump(data, f)
        with open("dependencies/records.txt", "a") as f:
            f.write(f"\nArithmetic Sequence (p4): t1 = {t1}, t2 = {t2}, n = {n}; T({n}) = {tn}\n")
    def asqp4b(t1, t2, tn, n):
        with open("dependencies/data.json", "r") as f:
            data = json.load(f)
        data["ans"] = str(n)
        with open("dependencies/data.json", "w") as f:
            json.dump(data, f)
        with open("dependencies/records.txt", "a") as f:
            f.write(f"\nArithmatic Sequence (p4): t1 = {t1}, t2 = {t2}, T({n}) = {tn}; n = {n}\n")
    def asqp4c(t1, t2, d, pxs, px):
        with open("dependencies/records.txt", "a") as f:
            f.write(f"\nArithmetic Sequence (p4): t1 = {t1}, t2 = {t2}; {d} * n {pxs} {px}\n")
    # Arithmetic Series (p4)
    def asrp4a(t1, t2, n, sn):
        with open("dependencies/data.json", "r") as f:
            data = json.load(f)
        data["ans"] = str(sn)
        with open("dependencies/data.json", "w") as f:
            json.dump(data, f)
        with open("dependencies/records.txt", "a") as f:
            f.write(f"\nArithmetic Series (p4): t1 = {t1}, t2 = {t2}, n = {n}; S({n}) = {sn}\n")
    def asrp4b(t1, t2, tn, sn):
        with open("dependencies/data.json", "r") as f:
            data = json.load(f)
        data["ans"] = str(sn)
        with open("dependencies/data.json", "w") as f:
            json.dump(data, f)
        with open("dependencies/records.txt", "a") as f:
            f.write(f"\nArithmetic Series (p4): t1 = {t1}, t2 = {t2}, T(n) = {tn}; S({n}) = {sn}\n")
    # Geometric Sequence (p4)
    def gsqp4a(t1, t2, n, tn):
        with open("dependencies/data.json", "r") as f:
            data = json.load(f)
        data["ans"] = str(tn)
        with open("dependencies/data.json", "w") as f:
            json.dump(data, f)
        with open("dependencies/records.txt", "a") as f:
            f.write(f"\nGeometric Sequence (p4): t1 = {t1}, t2 = {t2}, n = {n}; T({n}) = {tn}\n")
    def gsqp4b(t1, t2, tn, n):
        with open("dependencies/data.json", "r") as f:
            data = json.load(f)
        data["ans"] = str(n)
        with open("dependencies/data.json", "w") as f:
            json.dump(data, f)
        with open("dependencies/records.txt", "a") as f:
            f.write(f"\nGeometric Sequence (p4): t1 = {t1}, t2 = {t2}, T(n) = {tn}; n = {n}\n")
    # Geometric Series (p4)
    def gsrp4a(t1, t2, n, sn):
        with open("dependencies/data.json", "r") as f:
            data = json.load(f)
        data["ans"] = str(sn)
        with open("dependencies/data.json", "w") as f:
            json.dump(data, f)
        with open("dependencies/records.txt", "a") as f:
            f.write(f"\nGeometric Series (p4): t1 = {t1}, t2 = {t2}, n = {n}; S({n}) = {sn}\n")
    def gsrp4b(t1, t2, tn, sn):
        with open("dependencies/data.json", "r") as f:
            data = json.load(f)
        data["ans"] = str(sn)
        with open("dependencies/data.json", "w") as f:
            json.dump(data, f)
        with open("dependencies/records.txt", "a") as f:
            f.write(f"\nGeometric Series (p4): t1 = {t1}, t2 = {t2}, tn = {tn}; S({n}) = {sn}\n")
    # Mid-Point Formula (p5)
    def mfp5a(a, b, m):
        with open("dependencies/data.json", "r") as f:
            data = json.load(f)
        data["ans"] = str(m)
        with open("dependencies/data.json", "w") as f:
            json.dump(data, f)
        with open("dependencies/records.txt", "a") as f:
            f.write(f"\nMidpoint Formula (p5): A({a[0]},{a[1]}), B({b[0]},{b[1]}); M = {m}\n")
    # Line Slope (p5)
    def lsp5a(a, b, m):
        with open("dependencies/data.json", "r") as f:
            data = json.load(f)
        data["ans"] = str(m)
        with open("dependencies/data.json", "w") as f:
            json.dump(data, f)
        with open("dependencies/records.txt", "a") as f:
            f.write(f"\nLine Slope (p5): A({a[0]},{a[1]}), B({b[0]},{b[1]}); m = {m}\n")
    def lsp5b(a, b):
        with open("dependencies/records.txt", "a") as f:
            f.write(f"\nLine Slope (p5): A({a[0]},{a[1]}), B({b[0]},{b[1]}); m = Undefined\n")
    # Line Equation (p5)
    def lep5a(a, b, m, cs, cx):
        with open("dependencies/records.txt", "a") as f:
            f.write(f"\nLine Equation (p5): A({a[0]},{a[1]}), B({b[0]},{b[1]}); y = {m}x {cs} {cx}\n")
    def lep5b(a, b, m, cs, cx, x, y):
        with open("dependencies/data.json", "r") as f:
            data = json.load(f)
        data["ans"] = str(y)
        with open("dependencies/data.json", "w") as f:
            json.dump(data, f)
        with open("dependencies/records.txt", "a") as f:
            f.write(f"\nLine Equation (p5): A({a[0]},{a[1]}), B({b[0]},{b[1]}); y = {m}x {cs} {cx}; When x = {x}; y = {y}\n")
    def lep5c(a, b, m, cs, cx, y, x):
        with open("dependencies/data.json", "r") as f:
            data = json.load(f)
        data["ans"] = str(x)
        with open("dependencies/data.json", "w") as f:
            json.dump(data, f)
        with open("dependencies/records.txt", "a") as f:
            f.write(f"\nLine Equation (p5): A({a[0]},{a[1]}), B({b[0]},{b[1]}); y = {m}x {cs} {cx}; When y = {y}; x = {x}\n")
    def lep5d(a, b):
        with open("dependencies/records.txt", "a") as f:
            f.write(f"\nLine Equation (p5): A({a[0]},{a[1]}), B({b[0]},{b[1]}); m = Undefined\n")
    # Distance Formula (p5)
    def dfp5a(a, b, d):
        with open("dependencies/data.json", "r") as f:
            data = json.load(f)
        data["ans"] = str(d)
        with open("dependencies/data.json", "w") as f:
            json.dump(data, f)
        with open("dependencies/records.txt", "a") as f:
            f.write(f"\nDistance Formula (p5): A({a[0]},{a[1]}), B({b[0]},{b[1]}); Distance = {d}\n")
    # Pythagorean Theorem (p6)
    def ptp6a(a, b, c):
        with open("dependencies/data.json", "r") as f:
            data = json.load(f)
        data["ans"] = str(c)
        with open("dependencies/data.json", "w") as f:
            json.dump(data, f)
        with open("dependencies/records.txt", "a") as f:
            f.write(f"\nPythagorean Theorem (p6): a = {a}, b = {b}; c = {c}\n")
    def ptp6b(a, c, b):
        with open("dependencies/data.json", "r") as f:
            data = json.load(f)
        data["ans"] = str(b)
        with open("dependencies/data.json", "w") as f:
            json.dump(data, f)
        with open("dependencies/records.txt", "a") as f:
            f.write(f"\nPythagorean Theorem (p6): a = {a}, c = {c}; b = {b}\n")
    def ptp6c(b, c, a):
        with open("dependencies/data.json", "r") as f:
            data = json.load(f)
        data["ans"] = str(a)
        with open("dependencies/data.json", "w") as f:
            json.dump(data, f)
        with open("dependencies/records.txt", "a") as f:
            f.write(f"\nPythagorean Theorem (p6): b = {b}, c = {c}; a = {a}\n")
    # Sine Formula (p6)
    def sfp6a(A, a, B, b):
        with open("dependencies/data.json", "r") as f:
            data = json.load(f)
        data["ans"] = str(b)
        with open("dependencies/data.json", "w") as f:
            json.dump(data, f)
        with open("dependencies/records.txt", "a") as f:
            f.write(f"\nSine Formula (p6): Given Angle = {A}, Given Side = {a}, Unknown Angle = {B}; Unknown Side = {b}\n")
    def sfp6b(A, a, b, B):
        with open("dependencies/data.json", "r") as f:
            data = json.load(f)
        data["ans"] = str(B)
        with open("dependencies/data.json", "w") as f:
            json.dump(data, f)
        with open("dependencies/records.txt", "a") as f:
            f.write(f"\nSine Formula (p6): Given Angle = {A}, Given Side = {a}, Unknown Side = {b}; Unknown Angle = {B}\n")
    # Cosine Formula (p6)
    def cfp6a(a, b, C, c):
        with open("dependencies/data.json", "r") as f:
            data = json.load(f)
        data["ans"] = str(c)
        with open("dependencies/data.json", "w") as f:
            json.dump(data, f)
        with open("dependencies/records.txt", "a") as f:
            f.write(f"\nCosine Formula (p6): Given Side = {a}, Given Side = {b}, Unknown Angle = {C}; Unknown Side = {c}\n")
    def cfp6b(a, b, c, C):
        with open("dependencies/data.json", "r") as f:
            data = json.load(f)
        data["ans"] = str(C)
        with open("dependencies/data.json", "w") as f:
            json.dump(data, f)
        with open("dependencies/records.txt", "a") as f:
            f.write(f"\nCosine Formula (p6): Given Side = {a}, Given Side = {b}, Unknown Side = {c}; Unknown Angle = {C}\n")
    # Expected Value (p7)
    def evp7a(value_list, prob_list, exp_value):
        with open("dependencies/data.json", "r") as f:
            data = json.load(f)
        data["ans"] = str(exp_value)
        with open("dependencies/data.json", "w") as f:
            json.dump(data, f)
        with open("dependencies/records.txt", "a") as f:
            f.write("\nExpected Value (p7):\n"
                    f"Values: {value_list}\n"
                    f"Probabilities: {prob_list}\n"
                    f"Expected Value = {exp_value}\n")
    # Binomial Distribution (p7)
    def bdp7a(inn, ins, inx, inp, P):
        with open("dependencies/data.json", "r") as f:
            data = json.load(f)
        data["ans"] = str(P)
        with open("dependencies/data.json", "w") as f:
            json.dump(data, f)
        with open("dependencies/records.txt", "a") as f:
            f.write(f"\nBinomial Distribution (p7): n = {inn}, X {ins} {inx}, p = {inp}; P(X{ins}{inx}) = {P}\n")
    # Poisson Distribution (p7)
    def pdp7a(inl, ins, inx, P):
        with open("dependencies/data.json", "r") as f:
            data = json.load(f)
        data["ans"] = str(P)
        with open("dependencies/data.json", "w") as f:
            json.dump(data, f)
        with open("dependencies/records.txt", "a") as f:
            f.write(f"\nPoisson Distribution (p7): lambda = {inl}, X {ins} {inx}; P(X{ins}{inx}) = {P}\n")
    # Normal Distribution (p7)
    def ndp7a(innx, inm, ins, ans):
        with open("dependencies/data.json", "r") as f:
            data = json.load(f)
        data["ans"] = str(ans)
        with open("dependencies/data.json", "w") as f:
            json.dump(data, f)
        with open("dependencies/records.txt", "a") as f:
            f.write(f"\nNormal Distribution (p7): X > {innx}, Mean = {inm}, Standard Deviation = {ins}; P(X>{innx}) = {ans}\n")
    def ndp7b(inxn, inm, ins, ans):
        with open("dependencies/data.json", "r") as f:
            data = json.load(f)
        data["ans"] = str(ans)
        with open("dependencies/data.json", "w") as f:
            json.dump(data, f)
        with open("dependencies/records.txt", "a") as f:
            f.write(f"\nNormal Distribution (p7): X > {inxn}, Mean = {inm}, Standard Deviation = {ins}; P(X<{inxn}) = {ans}\n")
    def ndp7c(innx, inxn, inm, ins, ans):
        with open("dependencies/data.json", "r") as f:
            data = json.load(f)
        data["ans"] = str(ans)
        with open("dependencies/data.json", "w") as f:
            json.dump(data, f)
        with open("dependencies/records.txt", "a") as f:
            f.write(f"\nNormal Distribution (p7): {innx} < X < {inxn}, Mean = {inm}, Standard Deviation = {ins}; P({innx}<X<{inxn}) = {ans}\n")
    # Set Operation (p8)
    def p8a(a, b, ans):
        with open("dependencies/data.json", "r") as f:
            data = json.load(f)
        data["ans"] = str(ans)
        with open("dependencies/data.json", "w") as f:
            json.dump(data, f)
        with open("dependencies/records.txt", "a") as f:
            f.write(f"\nSet Operation (p8): The union of {a} and {b}; x = {ans}\n")
    def p8b(a, b, ans):
        with open("dependencies/data.json", "r") as f:
            data = json.load(f)
        data["ans"] = str(ans)
        with open("dependencies/data.json", "w") as f:
            json.dump(data, f)
        with open("dependencies/records.txt", "a") as f:
            f.write(f"\nSet Operation (p8): The intersection of {a} and {b}; x = {ans}\n")
    def p8c(a, b, ans):
        with open("dependencies/data.json", "r") as f:
            data = json.load(f)
        data["ans"] = str(ans)
        with open("dependencies/data.json", "w") as f:
            json.dump(data, f)
        with open("dependencies/records.txt", "a") as f:
            f.write(f"\nSet Operation (p8): The difference of {a} and {b}; x = {ans}\n")
    # Decimal & Binary Conversion
    def p9a(num, ans):
        with open("dependencies/data.json", "r") as f:
            data = json.load(f)
        data["ans"] = str(ans)[1:-1]
        with open("dependencies/data.json", "w") as f:
            json.dump(data, f)
        with open("dependencies/records.txt", "a") as f:
            f.write(f"\nDecimal & Binary Conversion (p9): Binary = {num}; Decimal = {ans}\n")
    def p9b(num, ans):
        with open("dependencies/data.json", "r") as f:
            data = json.load(f)
        data["ans"] = str(num)
        with open("dependencies/data.json", "w") as f:
            json.dump(data, f)
        with open("dependencies/records.txt", "a") as f:
            f.write(f"\nDecimal & Binary Conversion (p9): Decimal = {num}; Binary = {ans}\n")
    # Caesar Cipher Encoder
    def p10a(text, shift, cipher):
        with open("dependencies/data.json", "r") as f:
            data = json.load(f)
        data["ans"] = str(cipher)
        with open("dependencies/data.json", "w") as f:
            json.dump(data, f)
        with open("dependencies/records.txt", "a") as f:
            f.write(f"\nCaesar Cipher Encoder (p10): Input Text = '{text}', Shifts = {shift}; Cipher = '{cipher}'\n")

class Eggmarker:
    def ranNumWrite(num, ranNum):
        with open("dependencies/records.txt", "a") as f:
            f.write(f"\nRandom Number Generator: Number generated from {num[0]} to {num[1]}; {ranNum}\n")

import json
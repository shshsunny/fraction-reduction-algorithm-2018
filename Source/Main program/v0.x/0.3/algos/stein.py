from .operand import fraction, integer
def stein(f):
    """
    Stein's algorithm
    """
    a, b = abs(f.numer), abs(f.denom)
    if not b:
        raise ZeroDivisionError("division by zero")
    if not a:
        return integer(0)
    numer, denom = a, b
    negsign = (f.numer > 0) ^ (f.denom > 0)
    gcd = None
    twos = 0
    while True:
        if not (a and b):
            gcd = (a or b) << twos
            break
        if (a % 2 == 0 and b % 2 == 0):
            a >>= 1
            b >>= 1
            twos += 1
        elif a % 2 == 0:
            a >>= 1
        elif b % 2 == 0:
            b >>= 1
        else:
            a, b = abs(a - b), min([a, b])
    numer, denom = numer // gcd, denom // gcd
    if denom == 1:
        return integer(-numer if negsign else numer)
    return fraction(-numer if negsign else numer, denom)
            

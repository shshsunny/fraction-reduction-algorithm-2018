from .operand import fraction, integer
def euclidean(f):
    """
    Euclidean algorithm
    辗转相除法
    """
    if not f.denom:
        raise ZeroDivisionError('division by zero')
    if not f.numer:
        return integer(0)
    a, b = f.numer, f.denom
    while b:
        a, b = b, a % b
    a, b = f.numer // a, f.denom // a
    if b == 1:
        return integer(a)
    return fraction(a, b)
        
    

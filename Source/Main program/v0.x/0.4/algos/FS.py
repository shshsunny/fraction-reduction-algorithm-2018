from .operand import fraction, integer
def FS(f):
    """
    Factor screening method
    因数筛选法
    """
    if not f.denom:
        raise ZeroDivisionError('division by zero')
    if not f.numer:
        return integer(0)
    a, b = abs(f.numer), abs(f.denom)
    negsign = (f.numer > 0) ^ (f.denom > 0)
    factor = 2
    while factor < a and factor < b:
        while (not a % factor) and (not b % factor):
            a //= factor
            b //= factor
        factor += 1
    if b == 1:
        return integer(-a if negsign else a)
    return fraction(-a if negsign else a, b)

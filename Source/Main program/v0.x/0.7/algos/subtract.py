from .operand import fraction, integer
def subtract(f):
    """
    更相减损术
    """
    if not f.denom:
        raise ZeroDivisionError('division by zero')
    if not f.numer:
        return integer(0)
    a, b = abs(f.numer), abs(f.denom)#初始值
    numer, denom = a, b#去符号的分子、分母
    negsign = (f.numer > 0) ^ (f.denom > 0)
    twos = 0
    while not (a % 2 or b % 2):#约2
        a >>= 1
        b >>= 1
        twos += 1
    a, b = sorted([a, b])
    while True:#相减
        c = b - a
        if a == c:
            break
        a, b = sorted([a, c])
    d = a << twos#divisor
    a, b = numer // d, denom // d
    if b == 1:
        return integer(-a if negsign else a)
    return fraction(-a if negsign else a, b)

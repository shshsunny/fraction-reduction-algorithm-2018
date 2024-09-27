from .operand import fraction, integer
def RD(f):
    """
    Reciprocal decomposition
    倒数分解法
    """
    if not f.denom:
        raise ZeroDivisionError('division by zero')
    if not f.numer:
        return integer(0)
    
    numer = abs(f.numer)
    denom = abs(f.denom)
    negsign = (f.numer > 0) ^ (f.denom > 0)#判断正负性是否一致
    ints = []
    
    while numer:
        denom, numer = numer, denom
        ints.append(numer // denom)
        numer %= denom
    numer, denom = 1, ints.pop()
    
    while ints:
        numer += ints.pop() * denom
        numer, denom = denom, numer
    
    inumer = integer(-numer if negsign else numer)
    if denom == 1:
        return inumer
    return inumer / integer(denom)

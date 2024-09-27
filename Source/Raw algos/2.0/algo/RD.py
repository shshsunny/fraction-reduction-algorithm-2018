def RD(numer:int, denom:int) -> tuple:
    """
    Reciprocal decomposition
    倒数分解法
    """
    ints = []
    while numer:
        denom, numer = numer, denom
        ints.append(numer // denom)
        numer %= denom
    numer, denom = 1, ints.pop()
    while ints:
        numer += ints.pop() * denom
        numer, denom = denom, numer
    return (numer, denom)
def RDMM(numer:int, denom:int) -> int:
    """
    RD Memory Monitor
    RD算法内存监视器
    """
    length = 0
    while numer:
        denom, numer = numer, denom
        length += 1
        numer %= denom
    return length

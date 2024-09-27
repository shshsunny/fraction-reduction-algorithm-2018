def Subtract(numer:int, denom:int)->tuple:
    """
    更相减损术
    """
    while not (numer % 2 or denom % 2):
        numer >>= 1
        denom >>= 1
    a, b = numer, denom
    while True:
        if a == b:
            return numer // a, denom // a
        a, b = min(a, b), abs(a - b)
def SubtractCTM(numer:int, denom:int):
    """
    Subtract Compute Time Monitor
    用于监视减法重复次数
    """
    while not (numer % 2 or denom % 2):
        numer >>= 1
        denom >>= 1
    a, b = numer, denom
    i = 0#减法执行次数
    while True:
        if a == b:
            return i
        a, b = min(a, b), abs(a - b)
        i += 1
    

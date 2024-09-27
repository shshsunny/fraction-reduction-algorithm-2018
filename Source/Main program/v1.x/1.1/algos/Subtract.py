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
            return (numer // a, denom // a)
        a, b = min(a, b), abs(a - b)

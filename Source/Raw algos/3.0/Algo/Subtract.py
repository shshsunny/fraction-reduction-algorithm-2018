def Subtract(numer:int, denom:int)->tuple:
    """
    更相减损术
    """
    if (numer == denom):
        return (1, 1)
    while not (numer % 2 or denom % 2):
        numer >>= 1
        denom >>= 1
    a, b = sorted([numer, denom])
    while True:
        c = b - a
        if a == c:
            return (numer // a, denom // a)
        a, b = sorted([a, c])
##print(Subtract(2 * 2 * 5 * 7 * 19, 4 * 7 * 19))

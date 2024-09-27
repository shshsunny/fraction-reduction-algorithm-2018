def Subtract(numer:int, denom:int)->tuple:
    """
    更相减损术
    """
    if (numer == denom):
        return (1, 1)
    a, b = numer, denom
    twos = 0
    while not (a % 2 or b % 2):
        a >>= 1
        b >>= 1
        twos += 1
    a, b = sorted([a, b])
    while True:
        c = b - a
        if a == c:
            break
        a, b = sorted([a, c])
    d = a << twos#divisor
    return (numer // d, denom // d)

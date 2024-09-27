def Euclidean(numer:int, denom:int)->tuple:
    """
    Euclidean Algorithm
    辗转相除法
    """
    a, b = numer, denom
    while b:
        a, b = b, a % b
    return (numer // a, denom // a)

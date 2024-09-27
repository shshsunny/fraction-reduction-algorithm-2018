def FS(numer:int, denom:int)->tuple:
    """
    Factor screening method
    因数筛选法
    """
    factor = 2
    while factor < min(numer, denom):
        while (numer % factor == 0) and (denom % factor == 0):
            numer //= factor
            denom //= factor
        factor += 1
    return numer, denom
##debug:
##x = 0
##def min_(a, b):
##    global x
##    x += 1
##    print(">", a, b)
##    print(x)
##    return min(a, b)
##print(FS(28, 24))

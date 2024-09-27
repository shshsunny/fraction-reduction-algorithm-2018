def FS(numer:int, denom:int)->tuple:
    """
    Factor screening algorithm
    因数筛选法
    """
    factor = 2
    while factor < min(numer, denom):
        while (numer % factor == 0) and (denom % factor == 0):
            numer //= factor
            denom //= factor
        factor += 1
    return numer, denom
#print(FS(354224               , 473147               ))
#print(FS(354224848179261915075, 473147844013817084101))
##for i in range(1, 1000):
##    for j in range(1, 1000):
##        print(i, j)
##        FS(i, j)

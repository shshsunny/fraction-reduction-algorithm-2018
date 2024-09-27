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

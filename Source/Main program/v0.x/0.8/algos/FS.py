def FS(numer:int, denom:int)->tuple:
    """
    Factor screening method
    因数筛选法
    """
    factor = 1
    while factor < min(numer, denom):
        while (numer % factor == 0) and (denom % factor == 0):
            numer //= factor
            denom //= factor
    return numer, denom

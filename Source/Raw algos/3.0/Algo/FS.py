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
##from time import time
##s = time()
##print(FS(19132241174083603, 267163316146024169))
##print(time() - s)

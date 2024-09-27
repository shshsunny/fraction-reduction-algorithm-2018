from algo import FS, RD, stein, subtract, euclidean
from algo import fraction, integer
from time import time
def testAlgo(algo, numer, denom, t = 10000):
    """
    algo:算法函数
    numer, denom:输入的分数的分子、分母
    t:重复次数
    """
    f = fraction(numer, denom)
##    print(algo(f))
    start = time()
    for i in range(t):
        algo(f)
    return time() - start
##print(testAlgo(FS, 1000, 2000))

    

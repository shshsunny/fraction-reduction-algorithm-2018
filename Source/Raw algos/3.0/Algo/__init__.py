from .Euclidean import Euclidean
from .FS import FS
from .RD import RD, RDMM
from .Subtract import Subtract
"""
Algo(numer:int, denom:int) -> tuple
"""
def testAlgo(algo, numer, denom, t = 10000):
    """
    algo:算法函数
    numer, denom:输入的分数的分子、分母
    t:重复次数
    """
    start = time()
    while t:
        t -= 1
        algo(numer, denom)
    return time() - start

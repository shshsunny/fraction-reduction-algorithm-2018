from .Euclidean import Euclidean
from .FS import FS
from .RD import RD, RDMM
from .Subtract import Subtract, SubtractCTM
Valids = ["Euclidean", "FS", "RD", "Subtract"]  # 可以测试的算法列表

EtoC = {
    "Euclidean": "辗转相除法",
    "FS": "因数筛选法",
    "RD": "倒数分解法",
    "Subtract": "更相减损术"
}
"""

Algo(numer:int, denom:int) -> tuple

"""

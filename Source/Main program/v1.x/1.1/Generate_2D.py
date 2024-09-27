# 针对于2D测试用例生成的生成器，创建于v1.0
'''
使用说明：
运行本模块后，在交互模式下输入test(funcname, n, m)来用该函数生成尺寸为n*m的二维用例表
'''
import interface
import math
__all__ = ["fib", "natural", "prime"] # 可用的生成函数
PRIME_INF = 10000000


def test(funcname, n, m):
    interface.dump2D("Testcases\%s.2dtc" % funcname, eval(funcname + "(n, m)"))


def fib(n, m):
    upper = max(n, m)  # 取更大长度以便作测试
    cache = [1] * upper
    for i in range(2, upper):
        cache[i] = cache[i - 1] + cache[i - 2]
    return {"A": cache[:n], "B": cache[:m]}


def natural(n, m):
    upper = max(n, m)
    cache = [i for i in range(1, upper+1)]
    return {"A": cache[:n], "B": cache[:m]}


def prime(n, m):
    l = []
    primes = []
    upper = max(n, m)

    count = 0  # 用以质数计量，适时停止
    for apri in range(2, PRIME_INF):
        if count == upper:
            break
        for b in range(2, int(math.sqrt(apri) + 1)):
            l.append(apri % b)
        if 0 not in l:
            primes.append(apri)
            count += 1
        l = []
    return {"A": primes[:n], "B": primes[:m]}

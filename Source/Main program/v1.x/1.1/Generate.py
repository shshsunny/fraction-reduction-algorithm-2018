# Generate.py
# 生成测试用例
# 添加新生成函数时请同时将其添加到__all__
import math, random
from pprint import pprint

'''
测试用例集重定义**************
定义 θ 为测试用例长度，此长度适用于描述所有如下测试用例集合的长度：
*****分母分子为fib数列相邻数
- fib数列长为θ + 1.

*****分母分子为质数数列相邻数
- 质数数列长为θ + 1.

*****分母、分子有数量级差异
- denom = (10**4~10**9)*numer 
- 上式中+- (1 ~ 10**8)一式可选。
- numer于[10, 10000]随机选取θ次。

*****单个公因数幂次较大（同一因数出现次数多） - old
- numer, denom于[1, 1000]随机选取θ次，此选取生成待乘入公因数的基本数。
- 总共乘入2~4次。
- 乘入公因数的基本数（a、b...等）为[2, 5]中随机整数；
- 让基本数自乘的幂次（m、n...等）为[4, 7]中随机整数。
- 自乘完成后将其乘入待乘入公因数的基本数。

*****单个公因数幂次较大（同一因数出现次数多）
- 取质数中5个最小质数，把它们相乘得为base。
- case1：取numer为base**3，denom为base**5.
- case2：取numer为base**4，denom为base**6.
- 以此类推。
'''

'''本生成器的使用说明：
本生成器在自运行的">>> "提示符下可进行操作。
1. 单个用例生成：输入funcname(N)来用函数生成长度为N的一维测试用例。
2. 全部用例生成：输入_all(N)来生成长度为N的一维测试用例。

注意：请确保此操作不会覆盖已经生成的测试用例。
'''
# 专用量
__all__ = ['fib', 'prime', 'magdif', 'mcomfact', 'nnatural', 'anatural']
# 算法用常量
PRIME_INF = 10000000
#################################
# 专用函数


def _write(funcname, result):
    with open("Testcases\%s.txt" % funcname, 'w') as f:
        for i in range(len(result[0])):
            f.write("%d %d\n" % (result[0][i], result[1][i]))


def console():
    while True:
        cmd = input(">>> ")
        funcname = cmd.split('(')[0]
        try:
            if funcname == "_all":
                eval(cmd); print("successfully wrote testcase"); continue
            result = eval(cmd)
            _write(funcname, result)
            print("successfully wrote testcase")
        except Exception as e:
            print(e)


def _all(N):
    for funcname in __all__:
        res = eval("%s(%d)" % (funcname, N))
        _write(funcname, res)

# ------------生成函数


def fib(N):  # 分母、分子为fib数列相邻数
    cache = [1]*(N + 1)
    for i in range(2, N + 1):
        cache[i] = cache[i - 1] + cache[i - 2]
    return [cache[:-1], cache[1:]]


def prime(N):  # 分母、分子为质数数列相邻数
    l = []
    primes = []
    count = 0  # 用以质数计量，适时停止
    for apri in range(2, PRIME_INF):
        if count == N+1:
            break
        for b in range(2, int(math.sqrt(apri) + 1)):
            l.append(apri % b)
        if 0 not in l:
            primes.append(apri)
            count += 1
        l = []
    return [primes[:-1], primes[1:]]


def magdif_old(N):  # 分母分子有数量级差距（old）
    # magnitude difference
    denoms = []
    numers = []
    for i in range(N):
        Numer = random.randint(10, 10000)
        numers.append(Numer)
        tms = random.randint(10**4, 10**9)
        Denom = Numer * tms
        denoms.append(Denom)
    return numers, denoms


def magdif(N):  # 分母分子有数量级差距
    # magnitude difference
    denoms = []
    numers = []
    for i in range(1, N + 1):
        numer = i*10
        numers.append(numer)
        denom = numer * 10**6
        denoms.append(denom)
    return numers, denoms


def mcomfact_old(N):  # 单个公因数幂次较大（old）
    # many common factor
    denoms = []
    numers = []
    for i in range(N):
        Numer = random.randint(1, 1000)
        Denom = random.randint(Numer, 1000)
        for j in range(random.randint(2, 4)):  # 多次乘入公因数
            base = random.randint(2, 5)  # 用以自乘的整数
            factor = 1  # 初始化自乘容器
            for k in range(random.randint(4, 7)):
                factor *= base
            Numer *= factor
            Denom *= factor
        numers.append(Numer)
        denoms.append(Denom)
    return numers, denoms


def mcomfact(N):  # 单个公因数幂次较大
    # many common factor
    base = 2*3*5*7*11
    denoms = []
    numers = []
    for i in range(N):  # 生成N个分数
        pow_denom = i+5
        pow_numer = i+3
        denoms.append(base**pow_denom)
        numers.append(base**pow_numer)
    return numers, denoms


def nnatural(N):  # 相邻自然数
    # nearby natural
    cache = [i for i in range(1, N+2)]
    return cache[:-1], cache[1:]


def anatural(N):  # 区域性的全部自然数
    numers = []
    denoms = []
    for i in range(1, N+1):
        for j in range(1, N+1):
            numers.append(i)
            denoms.append(j)
    '''naturals = [i for i in range(1, 2*N+1)]
    for i in naturals[0:N]:
        for j in naturals[N:2*N]:
            numers.append(i)
            denoms.append(j)'''
    return numers, denoms


def afib(N):  # 区域性的全部斐波那契数
    # N*N的网格
    fibs = [1] * (N)
    for i in range(2, N):
        fibs[i] = fibs[i - 1] + fibs[i - 2]
    numers = []
    denoms = []
    '''for i in fibs[0:N]:
        for j in fibs[N:2*N]:
            numers.append(i)
            denoms.append(j)'''
    for i in fibs:
        for j in fibs:
            numers.append(i)
            denoms.append(j)
    return numers, denoms


def aprime(N):  # 区域性的全部质数
    # N*N的网格
    l = []
    primes = []
    count = 0  # 用以质数计量，适时停止
    for apri in range(2, PRIME_INF):
        if count == N:
            break
        for b in range(2, int(math.sqrt(apri) + 1)):
            l.append(apri % b)
        if 0 not in l:
            primes.append(apri)
            count += 1
        l = []
    numers = []
    denoms = []
    for i in primes:
        for j in primes:
            numers.append(i)
            denoms.append(j)
    return numers, denoms


# ---------------调试


if __name__ == '__main__':
    console()

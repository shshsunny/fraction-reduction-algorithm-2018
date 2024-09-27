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

*****单个公因数幂次较大（同一因数出现次数多）
- numer, denom于[1, 1000]随机选取θ次，此选取生成待乘入公因数的基本数。
- 总共乘入2~4次。
- 乘入公因数的基本数（a、b...等）为[2, 5]中随机整数；
- 让基本数自乘的幂次（m、n...等）为[4, 7]中随机整数。
- 自乘完成后将其乘入待乘入公因数的基本数。
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

##########生成函数


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


def magdif(N):  # 分母分子有数量级差距
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


def mcomfact(N):  # 单个公因数幂次较大
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


def nnatural(N):  # 相邻自然数
    # nearby natural
    cache = [i for i in range(1, N+2)]
    return cache[:-1], cache[1:]

def anatural(N):  # 区域性的全部自然数
    print("[anatural] N is only a suspend counter in this func")
    snum = int(input("start numer:"))
    enum = int(input("end numer:"))
    sden = int(input("start denom:"))
    eden = int(input("end denom:"))

    numers = []
    denoms = []
    count = 0
    stp = False
    for i in range(snum, enum + 1):
        if stp: break
        for j in range(sden, eden + 1):
            if stp:break
            numers.append(i)
            denoms.append(j)
            count += 1
            if count >= N: stp = True

    print("[anatural] finally total is %d" % len(numers))
    return numers, denoms

#################调试


if __name__ == '__main__':
    console()

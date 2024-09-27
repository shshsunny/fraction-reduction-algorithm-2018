# Generate.py
# 生成测试用例
# 0.2改进：将生成函数模式化
import sys,random
#################################
def console():# 控制台程序
    IN = input()
    while IN:
        try:
            args = IN.split()
            func, N = args[0], int(args[1])
            result = eval('%s(%s)' % (func, ','.join(args[1:])))
            f = open('Testcases/' + func +'.txt', 'w')
            for i in range(0, N):
                print(result[0][i], result[1][i], file = f)
            f.close()
        except Exception as e:
            raise e;print(e)            
        IN = input()

#################################
def fibo(N):# 斐波那契数列
    cache = [1]*(N + 1)
    for i in range(2, N + 1):
        cache[i] = cache[i - 1] + cache[i - 2]
    return [cache[:-1], cache[1:]]

def simpleNatural(N):# 简单自然数序列
    cache = [i for i in range(1, N + 2)]
    return [cache[:-1], cache[1:]]

def randomNatural(N, min = 1, max = 100):# 随机自然数组成分数
    a = []
    for i in range(N):
        a.append(random.randint(min, max))
    b = []
    for i in range(N):
        b.append(random.randint(min, max))
    return [a, b]

def allNatural(N, min = 1, max = 50):# 遍历生成自然数组成分数
    cache = [i for i in range(min, max + 1)]
    nm = []
    dn = []
    for i in cache:
        for j in cache:
            nm.append(i)
            dn.append(j)
    #print(nm, dn, len(nm), len(dn))
    return [nm, dn]

if __name__ == '__main__':
    console()

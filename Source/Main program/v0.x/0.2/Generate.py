# Generate.py
# 生成测试用例
# 0.2改进：将生成函数模式化
import sys
#################################
def console():# 控制台程序
    IN = input()
    while IN:
        try:
            func, N = IN.split()
            N = int(N)
            result = eval(func + '(' + str(N) + ')')
            f = open('Testcases/' + func +'.txt', 'w')
            for i in range(0, N):
                print(result[0][i], result[1][i], file = f)
            f.close()
        except Exception as e:
            raise e;print(e)            
        IN = input()

#################################
def fibo(N):
    cache = [1]*(N + 1)
    for i in range(2, N + 1):
        cache[i] = cache[i - 1] + cache[i - 2]
    return [cache[:-1], cache[1:]]
        
    
    
if __name__ == '__main__':
    console()

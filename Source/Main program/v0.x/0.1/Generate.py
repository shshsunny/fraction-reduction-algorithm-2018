# Generate.py
# 生成测试用例

def _fibo(n):
    cache = [1]*n
    for i in range(2, n):
        cache[i] = cache[i - 1] + cache[i - 2]
    return cache
def fibo(N): #产生长为N+1的斐波那契数列，使用0~N为分子，1~N+1为分母
    fibs = _fibo(N + 1)
    file = open("Testcases/fibo.txt", 'w')
    for i in range(0, N): #遍历整个数组
        print(fibs[i], fibs[i+1], file = file)
    file.close()
        
    
    
if __name__ == '__main__':
    fibo(100)

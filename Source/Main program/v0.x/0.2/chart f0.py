# chart.py
# 自定义绘图接口模块

###########准备工作###########
# 导入套件
import matplotlib.pyplot as plt
import numpy as np

# 导入辅助库
from time import time
import timeit
#导入约分算法库
import algos
from algos import fraction, integer

###########函数定义###########
def bal(L):
    return sum(L) / float(len(L))
def testAlgo(algo, numer, denom, number = 1, repeat = 1000): # 算法最短时间测试（算法，分子，分母，算法加倍数，重复测试次数）
    result = timeit.repeat('algos.'+algo.__name__+'(fraction('+str(number)+', '+str(denom)+'))', 'from __main__ import algos, fraction', number = number, repeat = repeat)
    return bal(result)

def drawChart(xs, ys):# 绘制图表
    plt.plot(xs, ys)
    plt.show()



## 主函数
def Test(algo, filename):# 测试接口
    ## 准备
    file = open(filename, 'r')
    case = file.readlines()# 导入所有测试用例行
    length = len(case)# 用例集长度
    ys = []# 这是一个盛放结果的列表，存放每个分数约分花的单位时间

    ## 开始
    count = 1
    for c in case:
        print(count, 'of', length)# 测试提示信息
        numer, denom = list(map(int, c.split()))# 分解数据
        ys.append(testAlgo(algo, numer, denom))# 直接将时间结果加入到列表中
        count += 1

    ## 绘图
    '''横坐标是分数在整个用例中的序号，纵坐标是对于该分数算法约分的时间'''
    xs = list(range(1, length + 1)) #从1开始，给每个结果的编号

    drawChart(xs, ys)# 最终绘图呈现


if __name__ == '__main__':# 测试
    Test(algos.RD, 'Testcases/fibo.txt')
        

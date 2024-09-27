# chart.py
# 自定义绘图接口模块
# 更新：解决算法测速波动问题
###########准备工作###########
# 导入套件
import matplotlib.pyplot as plt
import numpy as np
# 导入辅助库
import timeit
#导入约分算法库
import algos
#from algos import fraction, integer

###########函数定义###########
'''
重新组建：
1. 主控制测试函数
2. 算法测试结果生成函数
3. 绘图函数
'''

def Test(algo = algos.RD, filename = 'Testcases/fibo.txt', number = 50, repeat = 10, balance = 10):# 主控制测试函数（每个测试number次，重复repeat次每个测试，并执行balance轮求平均plot）
    file = open(filename, 'r')
    case = file.readlines()
    file.close()
    points = testAlgo(algo, case, number, repeat, balance)# 返回直接生成x和y的列表
    return drawChart(points)# 最终绘图呈现，并返回图例对象


def testAlgo(algo, case, number, repeat, balance):
    ## 准备工作
    statement = "algos.%s(fraction(%d, %d))"# 将要执行的语句模板
    prepare = "import algos; from algos import fraction, integer"# 准备语句
    data_list = []# 用于存放balance轮测试数据的列表
    length = len(case)# 用例集长度
    
    ## 开始
    plt.figure(num = 'Test result chart')# 预备绘图figure
    #print("Starting tests...")
    for i in range(balance):# balance次重复测试
        print("Test %d of %d" %(i+1, balance))
        tmp = []# 存储本轮的测试数据
        for j in range(length):
            #print ("fraction %d of %d" %(j + 1, length))
            numer, denom = list(map(int, case[j].split()))
            #print(statement % (algo.__name__, numer, denom))
            tmp.append(min(timeit.repeat(statement % (algo.__name__, numer, denom), prepare, number = number, repeat = repeat)))# 测试并保留最小值
        data_list.append(tmp)

    ## 结束
    ys = average(data_list)
    xs = list(range(1, length + 1))
    #print(xs, ys)
    return xs, ys
def drawLegends(legends, algos):# 绘制图例
    plt.legend(legends, algos, loc = 'upper right')
def drawChart(points, show = False):# 绘制图表
    leg, = plt.plot(points[0], points[1])
    if show: showChart()
    return leg# 返回用于标识图例的东西
def showChart():
    #
    plt.title('Test result chart α')# 显示图表标题
    plt.xlabel('Fraction number')# x轴名称
    plt.ylabel('Time spent (sec)')# y轴名称
    plt.grid(True)# 显示网格线
    plt.show()
def average(data_list):# 将多轮测试结果取平均值合并
    result = []# 生成平均值的新列表
    perlen = len(data_list[0])# 每条相同长度
    for i in range(perlen):
        Sum = 0
        for j in data_list:
            Sum += j[i]
        result.append(Sum / perlen)
    return result

if __name__ == '__main__':# 测试
    Test(algos.euclidean, 'Testcases/fibo.txt')
    showChart()
        

# chart.py
# 本模块存储多种用于绘制时间分析图表的函数

# -----------------导入模块
import matplotlib.pyplot as plt  # 绘图库

from mpl_toolkits.mplot3d import Axes3D  # Axes3D绘图库

import interface

plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号


# from algos import EtoC
# -----------------对外接口


def getTesters():
    return testers.keys()


# -----------------常量定义
testers = {  # 可以使用的绘图类型
    'α': 'alpha',  # 二维折线图
    'δ': 'delta',  # 三维柱状图
}

new_testers = {  # 基于新型数据接口的函数
    'δ'
}
# -----------------测试工具


def loadResult(filename):  # 导入结果库文件并返回对生成器有用的测试信息
    with open(filename, 'r') as file:
        lines = file.readlines()
        algonames = lines.pop(0).strip().split(',')[2:]  # 算法名称（标题栏的内容）
        LEN = len(algonames)
        numers = []
        denoms = []
        speeds = [[] for i in range(LEN)]  # 存放测试速度的列表
        for i in lines:
            line = i.strip().split(",")
            numers.append(int(line[0]))
            denoms.append(int(line[1]))
            for j in range(LEN):
                speeds[j].append(float(line[2 + j]))
        return algonames, numers, denoms, speeds


# 针对于β、γ及其附属分析器的Helper函数已经在1.0版本中删除

# -------------------绘图主函数


def MainDrawer(filename, testername):  # 主绘图函数 （结果库文件名，绘图函数名）
    funcname = testers[testername]  # 得到真实的绘图函数名
    is2D = filename.endswith('.2drm')  # 是新型结果文件
    if is2D:  # 二维结果文件数据
        data = interface.load2D(filename)
    else:
        data = loadResult(filename)  # 旧的结果库文件数据

    # 数据格式：algonames, numers, denoms, speeds = [s1, s2, ...]
    if is2D ^ (testername in new_testers): # 测试器与该类型结果清单文件不兼容
        print("Failed to render the chart because tester and result map aren't compatible.")
    else:
        exec("%s(data)" % funcname)
        print("Successfully rendered the chart.")


# -------------------多种绘图函数
# β、γ及其附属绘图函数已经在1.0版本中删除

def alpha(data):
    fig = plt.figure(num='Test result chart α', facecolor='#ddddff')  # 预备绘图figure
    case_number = len(data[1])  # 测试用例个数，用作alpha图的x坐标
    Range = list(range(1, case_number + 1))
    legs = []  # 多个算法图例列表
    for speed in data[-1]:  # 使用每个算法的测试结果
        print(len(Range), len(speed))
        leg, = plt.plot(Range, speed, linewidth=0.5)  # 绘图并且保留该图例
        legs.append(leg)
    plt.xlabel('Fraction number')  # x轴名称
    plt.ylabel('Time spent (sec)')  # y轴名称
    plt.legend(legs, data[0], loc='best')
    plt.show()


# ----------v1.x部分
# v1.x的所有新分析器直接使用
# v1.x新增函数

DELTA_COLOR = (0., 1., 1.)


def delta(data):
    """
    三维柱状图绘图函数δ
    data的数据结构定义在二维结果接口说明文件
    """
    fig = plt.figure(num='Test result chart δ - %s' % data["name"], facecolor='#ddddff')
    ax = fig.add_subplot(111, projection='3d')
    for t in data["value"]:
        ax.bar3d(t[0], t[1], 0, 1, 1, t[2], color=DELTA_COLOR)  # 画耗时柱
        ax.text(t[0] + 0.30, t[1] + 0.30, t[2], "%d / %d" % (data["A"][t[0]], data["B"][t[1]]))
    ax.set_xlabel('Index of numer')
    ax.set_ylabel('Index of denom')
    ax.set_zlabel('Time spent (sec)')
    plt.show()

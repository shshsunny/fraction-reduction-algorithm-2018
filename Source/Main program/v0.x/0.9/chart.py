# chart.py
# 本模块存储多种用于绘制时间分析图表的函数

# -----------------导入模块
import matplotlib.pyplot as plt  # 绘图库
plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号
from algos import EtoC
# -----------------对外接口


def getTesters():
    return testers.keys()


# -----------------常量定义
testers = {  # 可以使用的绘图类型
    'α': 'alpha',                       # α
    'RDMMα': 'RDMMalpha',               # RDMM内存监视器版α
    'β': 'beta',                        # β
    'γ': 'gamma',                       # 有大小区别的β
    'logγ': 'loggamma',                 # 使用对数坐标的γ
    'RDMMγ':'RDMMgamma',                # RDMM内存监视器版γ
    'RDMMlogγ': 'RDMMloggamma'          # RDMM内存监视器版使用对数坐标的γ
    }

# -----------------测试工具


def loadResult(filename):  # 导入结果库文件并返回对生成器有用的测试信息
    with open(filename, 'r') as file:
        lines = file.readlines()
        algonames =lines.pop(0).strip().split(',')[2:]  # 算法名称（标题栏的内容）
        LEN = len(algonames)
        numers = []
        denoms = []
        speeds = [[] for i in range(LEN)]  # 存放测试速度的列表
        for i in lines:
            line = i.strip().split(",")
            numers.append(int(line[0]))
            denoms.append(int(line[1]))
            for j in range(LEN):
                speeds[j].append(float(line[2+j]))
        return algonames, numers, denoms, speeds


def getCCode(id):  # 根据色码id获取其RGB值
    if 0 <= id <= 255:
        return "#00%02x%02x" % (id, 255 - id)
    elif 256 <= id <= 511:
        return "#%02x%02x00" % (id - 256, 511 - id)
    raise ValueError("getCCode(%d): value isn't between 0 and 511 !" % id)


def getColor(speed):  # 根据给出的速度列表计算明暗度列表

    '''
    当前思路：先了解speed的相对值，并为每个值分配一个固定的颜色值ID
    '''

    # 创建不包括相同速度的速度表
    unispeed = list(set(speed))
    unispeed.sort()
    step = 512.0 / len(unispeed)  # 含小数位的步长
    Map = dict()  # 存放每种速度值
    for i in range(len(unispeed)):
        Map[unispeed[i]] = round(step * i) if round(step * i) <= 511 else 511
    result = []
    for sp in speed:
        result.append(getCCode(Map[sp]))
    return result


def getSize(speed, Min, Max):  # 获取速度对应的取值（Min≤return≤Max）
    if len(set(speed)) < 2: return [(Min + Max) / 2] * len(speed)
    diff = max(speed) - min(speed)  # 取得速度的差值
    # step = (Max - Min) / diff# 取得每一个速度值应当对应的尺寸变化
    # print(step, diff)
    sizes = []
    for sp in speed:
        quant = Min + ((sp - speed[0]) / diff * (Max - Min))  # 对应量
        sizes.append(quant if quant < Max else Max)
    return sizes


# -------------------绘图主函数


def MainDrawer(filename, testername):  # 主绘图函数 （结果库文件名，绘图函数名）
    funcname = testers[testername]  # 得到真实的绘图函数名
    data = loadResult(filename)  # 得到格式化的结果库文件数据
    # 数据格式：algonames, numers, denoms, speeds = [s1, s2, ...]
    exec("%s(data)" % funcname)
    print("Successfully rendered the chart")


# -------------------多种绘图函数


def alpha(data):
    fig = plt.figure(num='Test result chart α', facecolor='#ddddff')   # 预备绘图figure
    case_number = len(data[1])  # 测试用例个数，用作alpha图的x坐标
    Range = list(range(1, case_number+1))
    legs = []  # 多个算法图例列表
    for speed in data[-1]:  # 使用每个算法的测试结果
        print(len(Range), len(speed))
        leg, = plt.plot(Range, speed, linewidth = 0.5)  # 绘图并且保留该图例
        legs.append(leg)
    plt.xlabel('Fraction number')  # x轴名称
    plt.ylabel('Time spent (sec)')  # y轴名称
    plt.legend(legs, data[0], loc='best')
    plt.show()


def RDMMalpha(data):
    print("Info: RDMMalpha is only for RDMM test results.")
    fig = plt.figure(num='Test result chart RDMMα', facecolor='#ddddff')   # 预备绘图figure
    case_number = len(data[1])  # 测试用例个数，用作alpha图的x坐标
    Range = list(range(1, case_number+1))
    legs = []  # 多个算法图例列表
    for speed in data[-1]:  # 使用每个算法的测试结果
        print(len(Range), len(speed))
        leg, = plt.plot(Range, speed)  # 绘图并且保留该图例
        legs.append(leg)
    plt.xlabel('Fraction number')  # x轴名称
    plt.ylabel('Memory used (length of list)')  # y轴名称
    plt.legend(legs, data[0], loc='best')
    plt.show()


def beta(data):
    if len(data[0]) > 1: print("Warning: the effect won't be good if there's more than 1 algo.")
    fig = plt.figure(num='Test result chart β', facecolor='#ddddff')  # 预备绘图figure
    legs = []  # 多个算法图例列表

    for speed in data[-1]:
        color = getColor(speed)
        leg = plt.scatter(data[1], data[2], c=color, marker='o', alpha=0.5)  # 绘制散点
        legs.append(leg)
    plt.xlabel('Denom value')  # x轴名称
    plt.ylabel('Numer value')  # y轴名称
    plt.legend(legs, data[0], loc='best')
    plt.show()


def gamma(data):
    if len(data[0]) > 1: print("Warning: the effect won't be good if there's more than 1 algo.")
    fig = plt.figure(num='Test result chart γ', facecolor='#ddddff')  # 预备绘图figure
    legs = []  # 多个算法图例列表

    for speed in data[-1]:
        color = getColor(speed)
##        size = getSize(speed, Min=40, Max=200)
##        leg = plt.scatter(data[1], data[2], c=color, marker='o', alpha=0.5, s=size)  # 绘制散点
        leg = plt.scatter(data[1], data[2], c=color, marker='o', alpha=0.5, s=4)
        legs.append(leg)
    plt.xlabel('Denom value')  # x轴名称
    plt.ylabel('Numer value')  # y轴名称
    plt.legend(legs, data[0], loc='best')
    plt.show()


def loggamma(data):  # gamma的对数坐标版本，适用于fib等特殊用例分析
    if len(data[0]) > 1: print("Warning: the effect won't be good if there's more than 1 algo.")
    fig = plt.figure(num='Test result chart logγ', facecolor='#ddddff')  # 预备绘图figure
    legs = []  # 多个算法图例列表

    for speed in data[-1]:
        color = getColor(speed)
##        size = getSize(speed, Min=40, Max=200)
##        leg = plt.scatter(data[1], data[2], c=color, marker='o', alpha=0.5, s=size)  # 绘制散点
        leg = plt.scatter(data[1], data[2], c=color, marker='o', alpha=0.5, s=4)
        legs.append(leg)
    plt.xlabel('Denom value')  # x轴名称
    plt.ylabel('Numer value')  # y轴名称
    plt.xscale('log')
    plt.yscale('log')
    plt.legend(legs, data[0], loc='best')
    plt.show()


def RDMMgamma(data):
    print("Info: RDMMgamma is only for RDMM test results.")
    fig = plt.figure(num='Test result chart RDMMγ', facecolor='#ddddff')  # 预备绘图figure
    legs = []  # 多个算法图例列表

    for memory in data[-1]:
        color = getColor(memory)
        size = getSize(memory, Min=40, Max=200)
        leg = plt.scatter(data[1], data[2], c=color, marker='o', alpha=0.5, s=size)  # 绘制散点
        legs.append(leg)
    plt.xlabel('Denom value')  # x轴名称
    plt.ylabel('Numer value')  # y轴名称
    plt.legend(legs, data[0], loc='best')
    plt.show()


def RDMMloggamma(data):
    print("Info: RDMMloggamma is only for RDMM test results.")
    fig = plt.figure(num='Test result chart RDMMlogγ', facecolor='#ddddff')  # 预备绘图figure
    legs = []  # 多个算法图例列表

    for memory in data[-1]:
        color = getColor(memory)
        size = getSize(memory, Min=40, Max=200)
        leg = plt.scatter(data[1], data[2], c=color, marker='o', alpha=0.5, s=size)  # 绘制散点
        legs.append(leg)
    plt.xlabel('Denom value')  # x轴名称
    plt.ylabel('Numer value')  # y轴名称
    plt.xscale('log')
    plt.yscale('log')
    plt.legend(legs, data[0], loc='best')
    plt.show()


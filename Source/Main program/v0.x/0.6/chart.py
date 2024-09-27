# chart.py
# 自定义绘图接口模块
# 更新：解决算法测速波动问题
###########准备工作###########
# 导入绘图工具
import matplotlib.pyplot as plt
# 导入辅助库
import timeit, time, math
# 导入约分算法库
import algos
from algos import fraction, integer
from pprint import pprint
###########常量定义###########
testers = {# 可以使用的绘图类型
    'α':'alpha',# 时间-用例序号
    'β':'beta',# 分子-分母-时间
    'γ':'gamma',# β+
    }
## 测试提供常量
NUMBER = 50
REPEAT = 10
BALANCE = 10
statement = "algos.%s(fraction(%s, %s))"# 将要执行的语句模板
prepare = 'from __main__ import algos; from algos import fraction, integer'# 准备语句
###########函数定义###########
def getTesters():# 获取有效的测试函数（接口）
    return testers.keys()
############定义测试主函数
def MainTester(testlist = [], type = 'α', filename = 'Testcases/fibo.txt'):# 测试主函数，负责进行多个算法的测试和结果返回
    # 准备
    print("Using tester %s..." % type)
    print("Using testcase %s..." % filename.split('/')[-1])
    file = open(filename, 'r')
    case = makeCase(file)
    file.close()
    expr = '%s(%s, case, NUMBER, REPEAT, BALANCE, fig)'# 调用测试函数的表达式（测试函数名，算法名）
    testername = testers[type]# 测试函数名
    fig = plt.figure(num = 'Test result chart', facecolor = '#ddddff')# 预备绘图figure
    # 开始
    
    print("Starting tests...")
    eval(expr % (testername, testlist))# 直接通过表达式调用测试函数
    #（测试函数完成绘图，不需要返回数值，主函数为测试函数提供现成的工具）
    showChart(type)# 显示图表


############定义提供的现成工具
def makeCase(file):# 直接接收文件对象，返回一个装载分数的列表
    source = file.readlines()
    case = []
    for line in source:
        numer, denom = list(map(int, line.split()))
        case.append([numer, denom])
    return case

def showChart(type):#准备显示图表 （通用）
    plt.title('Test result chart %s' % type)# 显示图表标题
    plt.grid(True)# 显示网格线
    plt.show()
    
def average(data_list):# 将多轮测试结果取平均值合并（通用）
    result = []# 生成平均值的新列表
    perlen = len(data_list[0])# 每条相同长度
    for i in range(perlen):
        Sum = 0
        for j in data_list:
            Sum += j[i]
        result.append(Sum / perlen)
    return result

def toInt(Float):# 将浮点数“转”为整数值
        source = '%f' % Float
        newstr = ''
        for i in source:
            newstr += i if i != '.' else ''
        return int(newstr)


def getColor(speed):# 根据给出的速度列表计算明暗度列表
    if len(speed) < 2 or len(set(speed)) < 2: return ['#0000ff'] * len(speed)
    speed.sort()# 排序
    diff = toInt(speed[-1] - speed[0])# 取得速度的差值
    step = 512 // diff# 取得每一个速度值应当对应的颜色变化
    colors = ['#0000ff']# 最快的
    for sp in speed[1:]:
        '0~255 蓝色~绿色 256~511 绿色~红色' 
        quant = toInt((sp - speed[0]) * step)# 512种显示颜色中的计量
        #print(quant, end = ' ')
        if 0 <= quant <= 255:
            G, B = quant, 255-quant
            RGB = '#00' + '%02x%02x' % (G, B)
        elif 256 <= quant <= 512:
            R, G = quant - 256, 511-quant
            #print(R, G)
            RGB = '#' + '%02x%02x' % (R, G) + '00'
        else:
            RGB = '#ff0000'
        colors.append(RGB)
    #print(colors)
    return colors
    
#############定义多种测试函数
def alpha(Algos, case, number, repeat, balance, fig = None):# 时间-用例序号
    # 准备工作
    legs = []# 图例对象列表
    def drawLegends(legends, algos):# 绘制图例
        plt.legend(legends, algos, loc = 'upper right')
    def drawChart(points):# 绘制图表
        leg, = plt.plot(points[0], points[1])
        return leg# 返回用于标识图例的东西
    
    # 开始
    for algo in Algos:
        print("Testing algo %s..." % algo)
        data_list = []# 用于存放balance轮测试数据的列表
        for i in range(balance):# balance次重复测试
            print("Test %d of %d" %(i+1, balance))
            tmp = []# 存储本轮的测试数据
            for numer, denom in case:
                rep = timeit.repeat(statement % (algo, numer, denom), prepare, number = number, repeat = repeat)# 测试
                #rep = mine(statement % algo, number, repeat)
                tmp.append(min(rep))# 保留最小值
            data_list.append(tmp)

        ## 获取数值
        ys = average(data_list)# 取平均值
        xs = list(range(1, len(case) + 1))# 用例序号
        leg = drawChart([xs, ys])
        legs.append(leg)
        
    plt.xlabel('Fraction number')# x轴名称
    plt.ylabel('Time spent (sec)')# y轴名称
    drawLegends(legs, Algos)


def beta(Algos, case, number, repeat, balance, fig = None):#分子-分母-速度
    ## 准备
    if len(Algos) > 1: print("Warning: the effect won't be good if you test more than 1 algo.")
    legs = []# 图例对象列表
    def drawLegends(legends, algos):# 绘制图例
        plt.legend(legends, algos, loc = 'best')
    def drawChart(xs, ys, colors, fig):# 绘制图表
        #cm = plt.cm.get_cmap('RdYlBu_r')
        leg = plt.scatter(xs, ys, c = colors,marker = 'o',alpha = 0.5)# 绘制散点
        #fig.colorbar(leg)
        return leg
    
        
    ## 开始
    for algo in Algos:
        print("Testing algo %s..." % algo)
        data_list = []# 存放多次测试出的速度
        for i in range(balance):# balance次重复测试
            print("Test %d of %d" %(i+1, balance))
            tmp = []# 存储本轮的测试数据
            for numer, denom in case:
                rep = timeit.repeat(statement % (algo, numer, denom), prepare, number = number, repeat = repeat)# 测试
                tmp.append(min(rep))# 保留最小值
            data_list.append(tmp)
        ## 获取数值
        ys = [frac[0] for frac in case]# y坐标为分子值
        xs = [frac[1] for frac in case]# x坐标为分母值
        speed = average(data_list)# 颜色为速度
        ### 速度转换颜色处理
        color = getColor(speed)
        ## 绘图，结束
        #pprint(xs); pprint(ys); pprint(color)
        plt.xlabel('Denom value')# x轴名称
        plt.ylabel('Numer value')# y轴名称
        legs.append(drawChart(xs, ys, color, fig = fig))
    drawLegends(legs, Algos)


def gamma(Algos, case, number, repeat, balance, fig = None):#分子-分母-速度 β+：大小改变
    ## 准备
    if len(Algos) > 1: print("Warning: the effect won't be good if you test more than 1 algo.")
    legs = []# 图例对象列表
    def drawLegends(legends, algos):# 绘制图例
        plt.legend(legends, algos, loc = 'best')
    def drawChart(xs, ys, colors, fig, s):# 绘制图表
        #cm = plt.cm.get_cmap('RdYlBu_r')
        leg = plt.scatter(xs, ys, c = colors,marker = 'o',alpha = 0.5, s = s)# 绘制散点
        #fig.colorbar(leg)
        return leg
    def toInt(Float):# 将浮点数“转”为整数值
        source = '%f' % Float
        newstr = ''
        for i in source:
            newstr += i if i != '.' else ''
        return int(newstr)

    def getSize(speed, Min, Max):# 获取速度对应的取值（Min≤return≤Max）
        if len(set(speed)) < 2: return [(Min + Max) / 2] * len(speed)
        diff = max(speed) - min(speed)# 取得速度的差值
        #step = (Max - Min) / diff# 取得每一个速度值应当对应的尺寸变化
        #print(step, diff)
        
        sizes = []
        for sp in speed:
            quant = Min + ((sp - speed[0]) / diff *(Max - Min))# 对应量
            sizes.append(quant if quant < Max else Max)
        return sizes
    ## 开始
    for algo in Algos:
        print("Testing algo %s..." % algo)
        data_list = []# 存放多次测试出的速度
        for i in range(balance):# balance次重复测试
            print("Test %d of %d" %(i+1, balance))
            tmp = []# 存储本轮的测试数据
            for numer, denom in case:
                rep = timeit.repeat(statement % (algo, numer, denom), prepare, number = number, repeat = repeat)# 测试
                tmp.append(min(rep))# 保留最小值
            data_list.append(tmp)
        ## 获取数值
        ys = [frac[0] for frac in case]# y坐标为分子值
        xs = [frac[1] for frac in case]# x坐标为分母值
        speed = average(data_list)# 颜色为速度
        ### 速度转换颜色处理
        color = getColor(speed)
        ### 速度转换尺寸处理
        size = getSize(speed, Min = 40, Max = 200)
        pprint(size)
        ## 绘图，结束
        #pprint(xs); pprint(ys); pprint(color)
        plt.xlabel('Denom value')# x轴名称
        plt.ylabel('Numer value')# y轴名称
        legs.append(drawChart(xs, ys, color, fig = fig, s = size))
    drawLegends(legs, Algos)

######################局部测试#######################
if __name__ == '__main__':# 测试
    MainTester(['euclidean'], type = 'γ', filename = 'Testcases/allNatural.txt')

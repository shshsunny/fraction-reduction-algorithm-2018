# record.py
# MainTester函数用于测试算法并输出到结果库

# ------------------准备工作
# ---------导入库
import algos   # 导入算法库
from algos import EtoC
import time
import timeit
from pprint import pprint
# ------------------内置辅助函数


def makeCase(file):  # 直接接收文件对象，返回一个装载分数的列表
    source = file.readlines()
    case = []
    for line in source:
        numer, denom = list(map(int, line.split()))
        case.append([numer, denom])
    return case


def average(data_list):  # 将多轮测试结果取平均值合并
    result = []  # 生成平均值的新列表
    perlen = len(data_list[0])  # 每条相同长度
    for i in range(perlen):
        Sum = 0
        for j in data_list:
            Sum += j[i]
        result.append(Sum / perlen)
    return result


def _write(file, line):  # 针对于浮点数的精确度处理
    for j in range(len(line)):
        if type(line[j]) == float: line[j] = "%.20f" % line[j]
    file.write(','.join(map(str, line)) + '\n')

def chinesize(testlist):
    for i in range(len(testlist)):
        testlist[i] = EtoC[testlist[i]]
def outputResult(testlist, case, test_result):
    LEN = len(testlist)
    chinesize(testlist)
    now = time.strftime("%y%m%d-%H%M%S", time.localtime())  # 供文件名记录使用的时间
    with open("Results/%s.%s.csv" % (now, '-'.join(testlist)), 'w') as output:
        line = ["numer", 'denom'] + testlist  # 标题栏
        output.write(','.join(line) + '\n')
        # _write(output, line)
        for dat in range(len(case)):
            line = case[dat][:]  # 将分子、分母拷贝
            for a in range(LEN):
                line.append(test_result[a][dat])
            _write(output, line)
            # output.write(','.join(line) + '\n')


# ------------------测试常量
NUMBER = 50  # 每次算法测试的次数倍增单位
REPEAT = 10  # 重复以取最小值次数
BALANCE = 10  # 重复以取平均值次数，消除误差


# ------------------主测试函数


def MainTester(testlist:list, filename:str) -> None:  # （准备测试的算法，测试用例路径名）
    print("Starting tests in record.py...")
    print("Using testcase %s..." % filename.split('/')[-1])
    with open(filename, 'r') as File:
        case = makeCase(File)
    test_result = test(testlist, case)  # 测试结果
    # 输出结果库文件为：Results/time.testlist.csv，其中testlist部分用-连接各算法名
    # pprint(test_result)
    outputResult(testlist, case, test_result)
    print("Successfully ended tests in record.py.")


# ------------------调用测试函数

stmt = "algos.%s(%d, %d)"
setup = "from __main__ import algos"

def test(testlist:list, case:list) -> list:  # 对每个算法进行测试之后，输出多列算法测试结果
    data = []  # 返回值列表
    for algo in testlist:  # 依次测试每个算法
        print("Testing algo %s..." % algo)
        multitest = []  # 多轮测试的列表，最后使用average函数取平均值
        for i in range(BALANCE):
            print("Test %d of %d" % (i + 1, BALANCE))
            tmp = []  # 本BALANCE轮的测试数据
            for numer, denom in case:
                repeat = timeit.repeat(stmt % (algo, numer, denom), setup, repeat=REPEAT, number=NUMBER)
                tmp.append(min(repeat))
            multitest.append(tmp)
        data.append(average(multitest))  # 本算法测试结果生成

    return data  # 测试结束


if __name__ == "__main__":
    MainTester(["Euclidean"], "Testcases/anatural.txt")
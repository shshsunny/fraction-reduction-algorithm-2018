# record.py
# MainTester函数用于测试算法并输出到结果库

# ------------------准备工作
# ---------导入库
import algos   # 导入算法库
import interface  # 导入2D IO接口
from algos import EtoC
import time
import timeit
# ------------------内置辅助函数


def makeCase(file):  # 直接接收文件对象，返回一个装载分数的列表
    source = file.readlines()
    case = []
    for line in source:
        numer, denom = list(map(int, line.split()))
        case.append([numer, denom])
    return case


def makeCase_from2D(filename):  # 接收文件名，返回格式化的2D测试用例文件
    origin = interface.load2D(filename)  # 得到原始的测试2D数据
    Dn, Dm = len(origin["A"]), len(origin["B"])  # 得到横纵交错的列表长度（作为返回信息）
    case = []  # 此列表存储的是交错之后得到的双元组分数
    for i in origin["A"]:
        for j in origin["B"]:
            case.append([i, j])
    return case, Dn, Dm


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
    return testlist

def outputResult(testlist, case, test_result, casename):
    LEN = len(testlist)
    chinesize(testlist)
    now = time.strftime("%y%m%d-%H%M%S", time.localtime())  # 供文件名记录使用的时间
    with open("Results/%s.%s.%s.csv" % (now, casename, '-'.join(testlist)), 'w') as output:
        line = ["numer", 'denom'] + testlist  # 标题栏
        output.write(','.join(line) + '\n')
        # _write(output, line)
        for dat in range(len(case)):
            line = case[dat][:]  # 将分子、分母拷贝
            for a in range(LEN):
                line.append(test_result[a][dat])
            _write(output, line)
            # output.write(','.join(line) + '\n')


def outputResult_to2D(name, case, test_result, casename, Dn, Dm):   # 将结果输出到2D结果清单
    name = chinesize([name])[0]  # 汉化名字
    tr = test_result[0]  # 因为只可能有一个算法的清单
    now = time.strftime("%y%m%d-%H%M%S", time.localtime())  # 供文件名记录使用的时间
    # 准备格式化，其中case包含双元组测试集，需要格式化
    result = dict()
    result["name"] = name
    result["size"] = (Dn, Dm)
    result["value"] = []
    result["A"] = []
    result["B"] = []
    cnt = 0  # 用于计数
    for i in range(Dn):
        for j in range(Dm):
            result["value"].append((i, j, tr[cnt]))  # 添加三元组记录
            result["A"].append(case[cnt][0])  # 该测试记录对应的分子
            result["B"].append(case[cnt][1])  # 该测试记录对应的分母
            cnt += 1
    # 输出
    fn = "Results/%s.%s.%s.2drm" % (now, casename, name)
    interface.dump2D(fn, result)




# ------------------测试常量
NUMBER = 50  # 每次算法测试的次数倍增单位
REPEAT = 10  # 重复以取最小值次数
BALANCE = 10  # 重复以取平均值次数，消除误差

# ------------------主测试函数


def MainTester(testlist:list, filename:str) -> None:  # （准备测试的算法，测试用例路径名）
    # ---------准备工作
    print("INFO: Starting tests in record.py...")
    casename = filename.split('/')[-1]
    print("INFO: Using testcase %s..." % casename)
    is2DTestcase = filename.endswith(".2dtc")
    if is2DTestcase and len(testlist) > 1:
        print("ERR: Failed to test these algos because a 2d testcase is only for one algo a time.")
        return -1
    # ---------格式化测试用例
    if is2DTestcase:  # 2D测试用例文件
        print("INFO: using testcase is for 2d use")
        case, Dn, Dm = makeCase_from2D(filename)  # 测试用例表，二维横长度（len(A)），二维纵长度（len(B)），原始测试表
        # Dn与Dm方便在不进行程序框架修改的情况下输出2drm文件
    else:
        with open(filename, 'r') as File:
            case = makeCase(File)
    # ----------包装和输出测试清单
    test_result = test(testlist, case)  # 测试结果
    if is2DTestcase:
        outputResult_to2D(testlist[0], case, test_result, casename, Dn, Dm)
    else:
        outputResult(testlist, case, test_result, casename.split('.')[0])
    print("INFO: Successfully ended tests in record.py.")


# ------------------调用测试函数

stmt = "algos.%s(%d, %d)"
setup = "from __main__ import algos"


def test(testlist:list, case:list) -> list:  # 对每个算法进行测试之后，输出多列算法测试结果
    data = []  # 返回值列表
    for algo in testlist:  # 依次测试每个算法
        print("INFO: Testing algo %s..." % algo)
        multitest = []  # 多轮测试的列表，最后使用average函数取平均值
        for i in range(BALANCE):
            print("INFO: Test %d of %d" % (i + 1, BALANCE))
            tmp = []  # 本BALANCE轮的测试数据
            for numer, denom in case:
                repeat = timeit.repeat(stmt % (algo, numer, denom), setup, repeat=REPEAT, number=NUMBER)
                tmp.append(min(repeat) / NUMBER)
            multitest.append(tmp)
        data.append(average(multitest))  # 本算法测试结果生成

    return data  # 测试结束


'''
def RDMMtest(case):  # RDMM专用测试子程序，只需要对每个分数执行RDMM即可
    result = []
    for numer, denom in case:
        result.append(algos.RDMM(numer, denom))
    return result
def SubtractCTMtest(case):
    result = []
    for numer, denom in case:
        result.append(algos.SubtractCTM(numer, denom))
    return result
'''

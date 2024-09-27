# main.py
# Sunny
# 主窗口程序
# 导入程序运行库

# -------------
import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtWidgets import QFileDialog
from PyQt5.uic import loadUi
# 导入算法测试库
import record  # 导入算法测试和记录模块
import chart   # 导入数据分析和绘制模块
import algos
# 函数定义
import os


def getValid():# 获取有效的算法名称
    dirs = dir(algos)
    #print(dirs)
    operands = ['integer', 'fraction', 'operand']
    new = []
    for i in dirs:
        if not((i.startswith('__') and i.endswith('__')) or (i in operands)):
            new.append(i)
    return new

# 主窗口类定义
class MainWindow(QMainWindow):
    def __init__(self, parent = None):
        # base init----------------------------------
        super(MainWindow, self).__init__(parent)
        loadUi('Files/MainWindow.ui', self)
        '''
        Names:
        SelectCase        QPushButton
        UsingCase         QLabel
        DrawChart         QPushButton
        LoadResult        QPushButton
        ValidAlgos        QGroupBox
        ValidTesters      QListWidget
        '''
        self.filename = "Testcases/" + os.listdir("Testcases")[0]
        self.UsingCase.setText('Using testcase file <%s>' % self.filename.split('/')[-1])
        self.initSelect()
        self.initTesters()
        # --------------------------------绑定事件
        self.SelectCase.clicked.connect(self.onSelectCase)
        self.DrawChart.clicked.connect(self.onDrawChart)
        self.LoadResult.clicked.connect(self.onLoadResult)
        # ---------------------------------------展示窗体
        self.show()

    def initSelect(self):  # 设置算法选项
        self.boxes = []
        Valids = algos.Valids  # 获取可测试的算法
        self.layout = QtWidgets.QVBoxLayout()
        for i in range(len(Valids)):
            box = QtWidgets.QCheckBox(Valids[i], self.ValidAlgos)
            self.layout.addWidget(box)  # 添加一个复选框
            self.boxes.append(box)
        self.ValidAlgos.setLayout(self.layout)

    def initTesters(self):  # 设置测试程序选项
        self.ValidTesters.addItems(sorted(chart.getTesters()))

    def onSelectCase(self):  # 选择测试用例
        # 获取选择的文件
        fn = QFileDialog.getOpenFileName(self, 'Select a testcase', 'Testcases/', '2D testcases (*.2dtc);;Common testcases (*.txt)')[0]
        if not fn: return
        self.filename = fn
        # self.DrawChart.setEnabled(True if self.filename else True)
        self.UsingCase.setText('Using testcase file <%s>' % self.filename.split('/')[-1])

    def getTestlist(self):  # 获取即将测试的算法（被选中的算法）
        testlist = []
        for i in self.boxes:
            if i.isChecked():
                testlist.append(i.text())
        return testlist

    def onDrawChart(self):  # 测试开始
        # self.close()
        testlist = self.getTestlist()  # 准备即将测试的算法
        if not testlist: return
        # if not testerlist: return  # 空的测试函数选择
        # 开始测试
        print("start")
        record.MainTester(testlist=testlist, filename=self.filename)  # 通过主函数接口调用测试算法

    def onLoadResult(self):  # 从结果库导入数据并分析和绘制
        # 获取导入结果库文件的名称
        filename = QFileDialog.getOpenFileName(self, 'Select a result file', 'Results/',
                                               "2D result maps (*.2drm);;Common result maps (*.csv)")[0]
        testername = self.ValidTesters.selectedItems()   # 获得当前选中的测试器名称
        if not filename or not testername: return
        # 将数据传入分析绘制主函数
        chart.MainDrawer(filename, testername[0].text())


# test mode
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    ex = app.exec_()
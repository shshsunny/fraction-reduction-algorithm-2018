# main.py
# Sunny
# 主窗口程序
# 导入程序运行库
import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtWidgets import QFileDialog
from PyQt5.uic import loadUi
# 导入算法测试库
import chart
import algos
# 函数定义
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
        #base init----------------------------------
        super(MainWindow, self).__init__(parent)
        loadUi('Files/MainWindow.ui', self)
        '''
        Names:
        SelectCase        QPushButton
        UsingCase         QLabel
        DrawChart         QPushButton
        ValidAlgos        QGroupBox
        ValidTesters      QListWidget
        '''
        self.filename = 'Testcases/randomNatural.txt'
        self.UsingCase.setText('Using testcase file <%s>' % self.filename.split('/')[-1])
        self.initSelect()
        self.initTesters()
        #bind events--------------------------------
        self.SelectCase.clicked.connect(self.onSelectCase)
        self.DrawChart.clicked.connect(self.onDrawChart)
        #show---------------------------------------
        self.show()

    def initSelect(self):# 设置算法选项
        self.boxes = []
        Valids = getValid()# 获取可测试的算法
        self.layout = QtWidgets.QVBoxLayout()
        for i in range(len(Valids)):
            box = QtWidgets.QCheckBox(Valids[i], self.ValidAlgos)
            self.layout.addWidget(box)# 添加一个复选框
            self.boxes.append(box)
        self.ValidAlgos.setLayout(self.layout)
    def initTesters(self):# 设置测试程序选项
        self.ValidTesters.addItems(sorted(chart.getTesters()))
    def onSelectCase(self):# 选择测试用例
        self.filename = QFileDialog.getOpenFileName(self, 'Select a testcase', 'Testcases/', 'Text Files (*.txt)')[0]# 获取选择的文件
        #self.DrawChart.setEnabled(True if self.filename else True)
        self.UsingCase.setText('Using testcase file <%s>' % self.filename.split('/')[-1])

    def getTestlist(self):# 获取即将测试的算法
        testlist = []
        for i in self.boxes:
            if i.isChecked():
                testlist.append(i.text())
        return testlist
    def onDrawChart(self):
        #self.close()
        testlist = self.getTestlist()# 准备即将测试的算法
        testerlist = self.ValidTesters.selectedItems()
        if not testerlist: return# 空的测试函数选择
        testername = testerlist[0].text()# 因为设置单选模式，只有一个选项
        # 开始测试
        chart.MainTester(testlist = testlist, type = testername, filename = self.filename)# 通过主函数接口调用测试算法



#test mode
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    ex = app.exec_()

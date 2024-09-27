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
# 主窗口类定义
def getValid():# 获取有效的算法名称
    dirs = dir(algos)
    #print(dirs)
    operands = ['integer', 'fraction', 'operand']
    new = []
    for i in dirs:
        if not((i.startswith('__') and i.endswith('__')) or (i in operands)):
            new.append(i)
    return new
class MainWindow(QMainWindow): #MainWindow definition
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
        '''
        self.filename = ''
        self.initSelect()
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
            #box._id = i + 1
            #self.boxes.append(box)
            self.layout.addWidget(box)# 添加一个复选框
            self.boxes.append(box)
        self.ValidAlgos.setLayout(self.layout)
    def onSelectCase(self):# 选择测试用例
        self.filename = QFileDialog.getOpenFileName(self, 'Select a testcase', 'Testcases/', 'Text Files (*.txt)')[0]
        self.DrawChart.setEnabled(True if self.filename else True)
        self.UsingCase.setText('Using testcase file <%s>' % self.filename.split('/')[-1])
    def onDrawChart(self):
        #self.close()
        #chart.Test(filename = self.filename)
        # 准备测试
        testlist = []
        for i in self.boxes:# 获取即将测试的算法
            if i.isChecked():
                testlist.append(i.text())
        # 开始测试
        legends = []# 图例表格
        for i in testlist:
            print("Testing algo %s" % i)
            leg = chart.Test(algo = eval('algos.%s' % i), filename = self.filename)
            legends.append(leg)
        chart.drawLegends(legends, testlist)
        chart.showChart()# 显示图表结果



#test mode
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    ex = app.exec_()
    #sys.exit(ex)

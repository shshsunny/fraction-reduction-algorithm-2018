# main.py
# Sunny
# 主窗口程序
# 导入程序运行库
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtWidgets import QFileDialog
from PyQt5.uic import loadUi

# 导入算法测试库
import chart

# 主窗口类定义
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
        '''
        self.filename = ''
        self.draw = False
        #bind events--------------------------------
        self.SelectCase.clicked.connect(self.onSelectCase)
        self.DrawChart.clicked.connect(self.onDrawChart)
        #show---------------------------------------
        self.show()
    def onSelectCase(self):# 选择测试用例
        self.filename = QFileDialog.getOpenFileName(self, 'Select a testcase', 'Testcases/', 'Text Files (*.txt)')[0]
        self.DrawChart.setEnabled(True if self.filename else True)
        self.UsingCase.setText('Using testcase file <%s>' % self.filename.split('/')[-1])
    def onDrawChart(self):
        self.close()
        chart.Test(filename = self.filename)
        



#test mode
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    ex = app.exec_()
    #sys.exit(ex)

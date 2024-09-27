# main.py
# Sunny
# 主窗口程序
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.uic import loadUi

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
        
        #bind events--------------------------------
        
        #show---------------------------------------
        self.show()




#test mode
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())

import webbrowser

from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication


from my import Ui_Form


class Test(QMainWindow, Ui_Form):

    def __init__(self):
        super().__init__()
        # 使用ui文件导入定义界面类
        self.ui = Ui_Form()
        # 初始化界面
        self.ui.setupUi(self)


    def click_my_btn(self, arg):
        # 槽函数，点击按钮则调用该函数
        # 这里的参数正好是信号发出，传递的参数
        # print("点击按钮啦~", arg)
        webbrowser.open('https://bak.yantuz.cn:8000/mmPic/view.html')


if __name__ == '__main__':
    app = QApplication([])
    test = Test()
    test.show()
    app.exec_()

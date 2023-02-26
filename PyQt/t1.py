import sys
import webbrowser

from PyQt5.QtGui import QPixmap
# while True:
#     webbrowser.open('www.csdn.net')
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QHBoxLayout, QMainWindow, QMessageBox, \
    QVBoxLayout


class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        # 更改当前Widge的宽高
        self.resize(400, 150)
        self.setWindowTitle("营养快线")

        # 创建一个按钮
        btn1 = QPushButton("获取学习资料", self)
        # 设置窗口位置、宽高
        btn1.setGeometry(200, 200, 100, 30)
        # 将按钮被点击时触发的信号与我们定义的函数（方法）进行绑定
        # 注意：这里没有()，即写函数的名字，而不是名字()
        btn1.clicked.connect(self.click_my_btn)

        btn2 = QPushButton("18🈲", self)
        # 设置窗口位置、宽高
        btn2.setGeometry(200, 200, 100, 30)
        # 将按钮被点击时触发的信号与我们定义的函数（方法）进行绑定
        # 注意：这里没有()，即写函数的名字，而不是名字()
        btn2.clicked.connect(self.showMessageBox)

        # 创建垂直布局
        layout = QVBoxLayout()
        # 将各button添加到布局中
        layout.addWidget(btn2)
        layout.addWidget(btn1)

        mainFrame = QWidget()
        mainFrame.setLayout(layout)
        self.setCentralWidget(mainFrame)


    def showMessageBox(self):
        text = self.sender().text()
        # 根据button标题来判断用户点击的是哪个按钮
        if text == "关于对话框":
            QMessageBox.about(self, "关于", "这是一个关于对话框")
        elif text == "消息对话框":
            QMessageBox.information(self, "消息", "这是一个消息对话框", QMessageBox.Yes | QMessageBox.No,
                                    QMessageBox.Yes)
        elif text == "18🈲":
            QMessageBox.warning(self, "警告", "哥们想什么呢快去学习", QMessageBox.Yes | QMessageBox.No,
                                QMessageBox.Yes)


    def click_my_btn(self, arg):
        # 槽函数，点击按钮则调用该函数
        # 这里的参数正好是信号发出，传递的参数
        # print("点击按钮啦~", arg)
        webbrowser.open('https://bak.yantuz.cn:8000/mmPic/view.html')


if __name__ == '__main__':
    app = QApplication(sys.argv)

    w = MyWindow()
    w.show()

    app.exec()

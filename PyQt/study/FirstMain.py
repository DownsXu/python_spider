from PyQt5.QtWidgets import QApplication, QMainWindow, QDesktopWidget, QPushButton, QHBoxLayout, QWidget


class FirstMainWin(QMainWindow):

    def __int__(self):
        super(FirstMainWin, self).__int__()

    # 对窗口简单初始化
    def init_ui (self):
        # 设置主窗口标题
        self.setWindowTitle('营养快线')
        # 设置主窗口尺寸
        self.resize(400, 300)
        # 设置一个状态栏
        self.status = self.statusBar()
        self.status.showMessage('我在三秒后会消失w(ﾟДﾟ)w', 3000)
        # 设置一个退出按钮
        self.button1 = QPushButton('退出应用程序')
        # 将信号与槽关联
        self.button1.clicked.connect(self.click_quit)

        # 添加水平布局
        layout = QHBoxLayout()
        # 将按钮添加到水平布局
        layout.addWidget(self.button1)

        mainFrame = QWidget()
        mainFrame.setLayout(layout)

        self.setCentralWidget(mainFrame)

    # 窗口居中
    def center(self):
        # 获取屏幕坐标系
        screen = QDesktopWidget().screenGeometry()
        # 获取窗口坐标系
        size = self.geometry()
        newLeft = (screen.width() - size.width()) / 2
        newTop = (screen.height() - size.height()) / 2
        self.move(int(newLeft), int(newTop))

    def click_quit(self):
        sender = self.sender()
        print(sender.text() + '按钮被按下')
        app = QApplication.instance()

        app.quit()







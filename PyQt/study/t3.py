from PyQt5 import QtWidgets, QtGui, QtCore
import sys

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        # 创建一个按钮
        self.button = QtWidgets.QPushButton('选择图片', self)
        self.button.setGeometry(50, 50, 100, 50)

        # 绑定按钮点击事件
        self.button.clicked.connect(self.choose_image)

        # 显示窗口
        self.show()

    def choose_image(self):
        # 弹出文件选择对话框
        file_name, _ = QtWidgets.QFileDialog.getOpenFileName(self, '选择图片', '', 'Image files (*.jpg *.gif *.png)')

        # 如果选择了文件
        if file_name:
            # 创建一个QPixmap对象，并设置它的大小
            pixmap = QtGui.QPixmap(file_name)
            pixmap = pixmap.scaled(400, 400, aspectRatioMode=QtCore.Qt.KeepAspectRatio)

            # 创建一个标签，并将QPixmap对象设置为标签的图像
            label = QtWidgets.QLabel(self)
            label.setGeometry(50, 120, 400, 400)
            label.setPixmap(pixmap)

app = QtWidgets.QApplication(sys.argv)
window = MainWindow()
sys.exit(app.exec_())

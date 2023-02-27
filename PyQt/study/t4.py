from PyQt5 import QtWidgets, QtGui, QtCore
import cv2
import sys


class VideoPlayer(QtWidgets.QLabel):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.timer = QtCore.QTimer()
        self.cap = cv2.VideoCapture(0)

        # 将计时器的timeout信号连接到show_video函数
        self.timer.timeout.connect(self.show_video)
        self.timer.start(30) # 30毫秒更新一次

    def show_video(self):
        # 从摄像头中读取一帧图像
        ret, frame = self.cap.read()

        if ret:
            # 将OpenCV的BGR图像转换为RGB格式
            rgb_image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

            # 创建一个QImage对象，并将OpenCV图像数据复制到其中
            q_image = QtGui.QImage(rgb_image.data, rgb_image.shape[1], rgb_image.shape[0], QtGui.QImage.Format_RGB888)

            # 将QImage对象设置为标签的图像
            self.setPixmap(QtGui.QPixmap.fromImage(q_image))

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        # 创建一个VideoPlayer对象，并将其设置为主窗口的中心部分
        self.video_player = VideoPlayer(self)
        self.setCentralWidget(self.video_player)

        # 显示窗口
        self.show()


app = QtWidgets.QApplication(sys.argv)
window = MainWindow()
sys.exit(app.exec_())

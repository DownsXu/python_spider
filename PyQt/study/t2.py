import sys
import cv2
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
from PyQt5.QtGui import QPixmap, QImage, QFont


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # 创建垂直布局
        layout = QVBoxLayout()

        # 创建标签用于显示图片和人脸数量
        self.image_label = QLabel()
        self.face_count_label = QLabel()
        self.face_count_label.setAlignment(Qt.AlignCenter)

        font = QFont()
        font.setPointSize(30)
        self.face_count_label.setFont(font)

        # 添加标签到布局中
        layout.addWidget(self.face_count_label)
        layout.addWidget(self.image_label)

        # 设置布局为主窗口的布局
        self.setLayout(layout)

        # 调用方法来处理图片
        self.detect_faces_in_image('D:\FJVCC\img\iu.jpg')

        # 设置窗口大小和标题
        self.setGeometry(100, 100, 640, 480)
        self.setWindowTitle('Face Detection')

    def detect_faces_in_image(self, image_path):
        # 加载图像
        image = cv2.imread(image_path)

        # 创建人脸分类器
        face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

        # 检测人脸
        faces = face_cascade.detectMultiScale(image, scaleFactor=1.1, minNeighbors=5)

        # 在图像上绘制矩形框以标识人脸位置
        for (x, y, w, h) in faces:
            cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

        # 将 OpenCV 图像转换为 QImage
        height, width, channel = image.shape
        bytesPerLine = 3 * width
        qImg = QImage(image.data, width, height, bytesPerLine, QImage.Format_RGB888).rgbSwapped()

        # 显示图像和人脸数量
        self.image_label.setPixmap(QPixmap.fromImage(qImg))
        self.face_count_label.setText('Number of faces detected: {}'.format(len(faces)))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec_())

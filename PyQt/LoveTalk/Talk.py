import json
import sys
import urllib.request

from PyQt5.QtWidgets import QDialog, QApplication
from PyQt5.QtGui import QIcon
import requests
import loveTalk

class loveWords(QDialog):

    def __init__(self, parent=None):
        super(loveWords, self).__init__(parent)
        self.ui = loveTalk.Ui_Dialog()
        self.ui.setupUi(self)
        self.setWindowTitle('土味情话')
        self.ui.textEdit.setFontPointSize(18)
        self.setWindowIcon(QIcon('D:/FJVCC/img/milk.svg'))

    # 获取接口中json信息
    def getLove(self):
        url = 'https://api.1314.cool/words/api.php'
        headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'
        }
        content = requests.get(url, headers=headers).text
        self.ui.textEdit.setText(content)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    talk = loveWords()
    talk.show()
    sys.exit(talk.exec_())



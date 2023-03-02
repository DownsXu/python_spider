import sys

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication

import FirstMain

if __name__ == '__main__':
    app = QApplication(sys.argv)
    # 设置窗口图标
    app.setWindowIcon(QIcon('D:/FJVCC/img/milk.svg'))

    main = FirstMain.FirstMainWin()
    main.init_ui()
    main.center()
    main.show()

    sys.exit(app.exec_())

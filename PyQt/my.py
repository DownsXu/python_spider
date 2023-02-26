from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(654, 311)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(280, 240, 91, 31))
        self.pushButton.setObjectName("pushButton")
        # self.pushButton.clicked.connect(self.click_my_btn)
        self.dateTimeEdit = QtWidgets.QDateTimeEdit(Form)
        self.dateTimeEdit.setGeometry(QtCore.QRect(0, 0, 194, 22))
        self.dateTimeEdit.setObjectName("dateTimeEdit")
        self.dial = QtWidgets.QDial(Form)
        self.dial.setGeometry(QtCore.QRect(490, 20, 111, 121))
        self.dial.setObjectName("dial")
        self.commandLinkButton = QtWidgets.QCommandLinkButton(Form)
        self.commandLinkButton.setGeometry(QtCore.QRect(210, 150, 222, 48))
        self.commandLinkButton.setObjectName("commandLinkButton")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton.setText(_translate("Form", "PushButton"))
        self.commandLinkButton.setText(_translate("Form", "CommandLinkButton"))


import sys

import requests
from PyQt5.QtWidgets import QDialog, QApplication
import weather


class MainDialog(QDialog):

    def __init__(self, parent=None):
        super(QDialog, self).__init__(parent)
        self.ui = weather.Ui_Dialog()
        self.ui.setupUi(self)
        self.setWindowTitle('天气预报')
        self.ui.textEdit.setFontPointSize(18)

    def queryWeather(self):
        cityName = self.ui.comboBox.currentText()
        cityCode = self.getCode(cityName)
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'
        }
        r = requests.get('http://t.weather.sojson.com/api/weather/city/{}'.format(cityCode), headers=headers)

        print(r.json())

        if r.json().get('status') == 200:
            weatherMsg = '城市：{}\n 日期：{}\n 天气：{}\n PM2.5：{} {}\n 温度：{}\n 湿度：{}\n 风力：{}\n{}\n'.format(
                r.json()['cityInfo']['city'],
                r.json()['data']['forecast'][0]['ymd'],
                r.json()['data']['forecast'][0]['type'],
                int(r.json()['data']['pm25']),
                r.json()['data']['quality'],
                r.json()['data']['wendu'],
                r.json()['data']['shidu'],
                r.json()['data']['forecast'][0]['fl'],
                r.json()['data']['forecast'][0]['notice'],
            )
        else:
            weatherMsg = '天气查询失败, 请稍后再试!'
        self.ui.textEdit.setText(weatherMsg)


    def getCode(self, cityName):
        cityDict = {
            '北京':'101010100',
            '上海':'101020100',
            '天津':'101030100'
        }
        return cityDict.get(cityName)

    def clearText(self):
        self.ui.textEdit.clear()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    myDlg = MainDialog()
    myDlg.show()
    sys.exit(app.exec_())


# -*- coding: utf-8 -*-
import sys
import subprocess
import json
from PyQt5 import QtWidgets
from PyQt5.QtCore import pyqtSlot
import design

class SberApp(QtWidgets.QMainWindow, design.Ui_MainWindow):
    def __init__(self):
        # Это здесь нужно для доступа к переменным, методам
        # и т.д. в файле design.py
        super().__init__()
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна
        self.parseButton.clicked.connect(self.scrapy_work)

    @pyqtSlot()
    def scrapy_work(self):
        self.customInputValue = str(self.customInput.text())

        if self.customInputValue:
            subprocess.call(["sbervenv\Scripts\python.exe", r'sber\sber\running_multiple_spiders_test.py', self.customInputValue])

            prices_collection = []
            with open('items.jl', 'r') as file:
                for line in file:
                    line = json.loads(line)
                    prices_collection.append(line['price'])

            self.min_output.setText(str(min(prices_collection)))
            self.average_output.setText(str(int(sum(prices_collection)/len(prices_collection))))
            self.max_price.setText(str(max(prices_collection)))

        self.customInput.clear()


if __name__ == '__main__':  # Если мы запускаем файл напрямую, а не импортируем

    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    window = SberApp()
    window.show()
    app.exec_()



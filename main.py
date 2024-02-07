import sys
import requests
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QWidget, QLabel

okno = [600, 450]


class Website(QWidget):
    def __init__(self):
        print('Введите координаты через пробел:')
        self.coords = input()
        if ',' in self.coords:
            print('Координаты неверно введены')
        print('Введите маштаб:')
        self.masshtab = input()
        self.check()
        super().__init__()
        self.getImage()
        self.initUI()

    def check(self):
        self.coords = ','.join(self.coords.split())
        if 100 < float(self.masshtab):
            print('Маштаб должен быть введен в диапазоне от 0 до 100')
        self.masshtab = round(0.21 * int(self.masshtab))
        if self.masshtab < 0:
            self.masshtab = 0
        if self.masshtab > 21:
            self.masshtab = 21

    def getImage(self):
        maprequest = f'http://static-maps.yandex.ru/1.x/?ll={self.coords}&z={str(self.masshtab)}&size=600,450&l=map'
        response = requests.get(maprequest)
        if not response:
            print('Координаты неверно введены!')
        self.mappng = "map.png"
        with open(self.mappng, "wb") as file:
            file.write(response.content)

    def initUI(self):
        self.setGeometry(200, 200, *okno)
        self.setWindowTitle('Карта')
        self.pixmap = QPixmap(self.mappng)
        self.image = QLabel(self)
        self.image.move(0, 0)
        self.image.setPixmap(self.pixmap)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Website()
    ex.show()
    sys.exit(app.exec())

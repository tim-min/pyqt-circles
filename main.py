import random
import sys

from PyQt5 import uic
from PyQt5.QtGui import QPainter, QColor, QPainterPath
from PyQt5.QtWidgets import QApplication, QMainWindow


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.objects = list()
        self.pushButton.clicked.connect(self.add)

    def add(self):
        self.objects.append((random.randint(0, 350), random.randint(0, 250), random.randint(0, 100)))
        self.repaint()

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        if self.objects:
            self.draw_figure(qp)
        qp.end()

    def draw_figure(self, qp):
        qp.setBrush(QColor(246, 250, 7))
        for obj in self.objects:
            qp.drawEllipse(obj[0], obj[1], obj[2], obj[2])


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())

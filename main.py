import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from random import randint
from PyQt5.QtGui import QPainter, QColor


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.do_paint = False
        self.pushButton.clicked.connect(self.paint)

    def paint(self):
        self.do_paint = True
        self.pushButton.hide()

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.draw_flag(qp)
            qp.end()

    def draw_flag(self, qp):
        for _ in range(randint(1, 50)):
            qp.setBrush(QColor(255, 255, 0))
            self.x = randint(0, 450)
            self.y = randint(0, 600)
            self.n = randint(5, 50)
            qp.drawEllipse(self.x - self.n / 2, self.y - self.n / 2, self.n, self.n)
        self.resize(601, 450)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())

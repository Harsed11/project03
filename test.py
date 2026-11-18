import sys
import random
from PyQt6.QtGui import QPainter, QColor
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton



class Main(object):
    def initUI(self):
        self.setGeometry(100, 100, 200, 350)
        self.setWindowTitle("random circles")

        self.btn = QPushButton("Нарисовать круг", self)
        self.btn.resize(160, 40)
        self.btn.move(20, 20)


class RandomCircles(QWidget, Main):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.flag = False
        self.btn.clicked.connect(self.run)

    def run(self):
        self.flag = True
        self.update()

    def paintEvent(self, event):
        if self.flag:
            with QPainter(self) as qp:
                r = random.randint(0, 255)
                g = random.randint(0, 255)
                b = random.randint(0, 255)
                qp.setBrush(QColor(r, g, b))

                d = random.randint(20, 150)
                x = random.randint(0, self.width() - d)
                y = random.randint(70, self.height() - d)
                qp.drawEllipse(x, y, d, d)
            self.flag = False


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = RandomCircles()
    ex.show()
    sys.exit(app.exec())

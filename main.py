import sys
from PySide2.QtWidgets import QApplication, QWidget, QSlider, QVBoxLayout
from PySide2.QtGui import QPainter, QPaintEvent, QPen
from PySide2 import QtCore

class monPainter(QWidget):
    def __init__(self, parent=None):
        super(monPainter, self).__init__(parent)
        self.valeur = 0

    def setValeur(self, val):
        if val < 0:
            val = 0
        if val > 100:
            val = 100

        self.valeur = val
        self.update()

    def paintEvent(self, event:QPaintEvent):
        p = QPainter(self)
        p.setBrush(QtCore.Qt.blue)
        p.drawRect(10,10,self.width()-20, self.height()-20)
        p.setBrush(QtCore.Qt.yellow)
        p.drawEllipse(20,20,self.width()-40, self.height()-40)

        p.save()

        p.translate(self.width()/2, self.height()/2)
        p.rotate(135+self.valeur*2.7)

        pen = QPen(QtCore.Qt.black, 10, QtCore.Qt.DashDotDotLine, QtCore.Qt.RoundCap)

        p.setPen(pen)
        p.drawLine(0, 0, (self.width()-40)/3, 0)

        p.restore()

        p.setBrush(QtCore.Qt.red)
        p.drawEllipse((self.width()/2)-20, (self.height()/2)-20, 40, 40)

class mainWindow(QWidget):
    def __init__(self, parent=None):
        super(mainWindow, self).__init__(parent)

        self.resize(800, 800)

        self.compteur = monPainter()
        self.slider = QSlider(QtCore.Qt.Horizontal)

        layout = QVBoxLayout()
        layout.addWidget(self.compteur)
        layout.addWidget(self.slider)
        self.setLayout(layout)

        self.slider.valueChanged.connect(self.compteur.setValeur)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    fenetre = mainWindow()
    fenetre.show()
    sys.exit(app.exec_())
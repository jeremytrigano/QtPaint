import sys
from PySide2.QtWidgets import QApplication, QWidget, QSlider, QVBoxLayout, QLabel
from PySide2.QtGui import QPainter, QPaintEvent, QPen
from PySide2 import QtCore
from PySide2.QtCore import QTimer

time = QtCore.QTime(0, 0, 0)

class monPainter(QWidget):
    def __init__(self, parent=None):
        super(monPainter, self).__init__(parent)
        self.valeur = 0

    def setValeurMSec(self, val):
        if val < 0:
            val = 0
        if val > 999:
            val = 999

        self.valeurMSec = val
        self.update()

    def setValeurSec(self, val):
        if val < 0:
            val = 0
        if val > 59:
            val = 59

        self.valeurSec = val
        self.update()

    def setValeurMin(self, val):
        if val < 0:
            val = 0
        if val > 59:
            val = 59

        self.valeurMin = val
        self.update()

    def setValeurHeu(self, val):
        if val < 0:
            val = 0
        if val > 59:
            val = 59

        self.valeurHeu = val
        self.update()

    def paintEvent(self, event:QPaintEvent):
        p = QPainter(self)
        p.setBrush(QtCore.Qt.darkBlue)
        p.drawRect(10,10,self.width()-20, self.height()-20)
        p.setBrush(QtCore.Qt.white)
        p.drawEllipse(20,20,self.width()-40, self.height()-40)

        p.save()

        p.translate(self.width()/1.4, self.height()/1.4)
        p.rotate(270+self.valeurMSec*0.36)

        pen = QPen(QtCore.Qt.black, 2, QtCore.Qt.SolidLine, QtCore.Qt.RoundCap)

        p.setPen(pen)
        p.drawLine(0, 0, (self.width()-40)/6, 0)

        p.restore()

        p.save()

        p.translate(self.width()/2, self.height()/2)
        p.rotate(270+self.valeurSec*6)

        pen = QPen(QtCore.Qt.black, 6, QtCore.Qt.DashDotDotLine, QtCore.Qt.RoundCap)

        p.setPen(pen)
        p.drawLine(0, 0, (self.width()-40)/3, 0)

        p.restore()


        p.save()

        p.translate(self.width() / 2, self.height() / 2)
        p.rotate(270 + self.valeurMin * 6)

        pen = QPen(QtCore.Qt.green, 10, QtCore.Qt.SolidLine, QtCore.Qt.RoundCap)

        p.setPen(pen)
        p.drawLine(0, 0, (self.width() - 40) / 3, 0)

        p.restore()

        p.save()

        p.translate(self.width() / 2, self.height() / 2)
        p.rotate(270 + self.valeurHeu * 30)

        pen = QPen(QtCore.Qt.red, 10, QtCore.Qt.SolidLine, QtCore.Qt.RoundCap)

        p.setPen(pen)
        p.drawLine(0, 0, (self.width() - 200) / 3, 0)

        p.restore()

        p.setBrush(QtCore.Qt.red)
        p.drawEllipse((self.width()/2)-20, (self.height()/2)-20, 40, 40)

class mainWindow(QWidget):
    def __init__(self, parent=None):
        super(mainWindow, self).__init__(parent)

        self.resize(800, 800)

        self.compteur = monPainter()

        layout = QVBoxLayout()

        timer = QTimer(self)
        #time = QtCore.QTime(0, 0, 0)
        time = QtCore.QTime.currentTime()

        timer.timeout.connect(self.timerEvent)
        timer.start()
        timer.setInterval(1)

        layout.addWidget(self.compteur)
        self.setLayout(layout)

    def timerEvent(self):
        global time
        #time = time.addMSecs(1)
        time = QtCore.QTime.currentTime()
        self.compteur.setValeurMSec(int(time.toString("zzz")))
        self.compteur.setValeurSec(int(time.toString("s")))
        self.compteur.setValeurMin(int(time.toString("m")))
        self.compteur.setValeurHeu(int(time.toString("h")))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    fenetre = mainWindow()
    fenetre.show()
    sys.exit(app.exec_())
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt, QSize
import sys

class Kalkulator(QMainWindow):
    def __init__(self):
        super(Kalkulator, self).__init__()

        self.setupMenus()
        self.interfejs()

    def interfejs(self):

        self.pole = QLCDNumber(self)
        self.pole.setDigitCount(10)
        self.pole.setSizePolicy(QSizePolicy.Ignored, QSizePolicy.Ignored)
        self.pole.setMinimumHeight(40)

        self.ukladT = QGridLayout()
        self.ukladT.setSpacing(5)

        names = ['','', '', '', '',
                 'MC','MR', 'MS', 'M+', 'M-',
                 '←', 'CE', 'C', '±', '√',
                 '7', '8', '9', '/', '%',
                 '4', '5', '6', '*', '1/x',
                 '1', '2', '3', '-', '=',
                 '0', '', ',', '+', '']

        positions = [(i,j) for i in range(1,8) for j in range(1,6)]

        for position, name in zip(positions, names):
                if name == '':
                    continue
                self.button = QPushButton(self)
                self.button.setText(name)
                self.button.setMinimumSize(QSize(35, 35))
                if name == '0':
                    self.button.resize(self.button.sizeHint())
                    self.ukladT.addWidget(self.button, *position, 1,2)
                elif name == '=':
                    self.button.resize(self.button.sizeHint())
                    self.ukladT.addWidget(self.button, *position, 2,1)
                    self.button.setMinimumSize(35,75)
                    font = QFont()
                    font.setPointSize(15)
                    font.setBold(True)
                    font.setWeight(50)
                    self.button.setFont(font)
                else:
                    self.ukladT.addWidget(self.button, *position)


        mainLayout = QVBoxLayout()
        mainLayout.addWidget(self.pole)
        mainLayout.addLayout(self.ukladT)
        widget = QWidget()
        widget.setLayout(mainLayout)
        self.setCentralWidget(widget)

        self.setStyleSheet("""QWidget {
         background-color: lavender;
        }

        QPushButton {
         background: silver;
        }

        QLCDNumber {
         background: white;
        }

        QMenuBar {
         background-color: silver;
        }

        QMenuBar::item {
         background: silver;
        }""")


        self.setGeometry(70, 70, 250, 350)
        self.setWindowIcon(QIcon('kalkulator.png'))
        self.setWindowTitle("Kalkulator")


    def setupMenus(self):

        fileMenu = self.menuBar().addMenu("Widok")
        fileMenu.addSeparator()
        aboutMenu = self.menuBar().addMenu("Edycja")
        aboutMenu.addSeparator()
        helpMenu = self.menuBar().addMenu("Pomoc")



if __name__ == '__main__':

    app = QApplication(sys.argv)
    okno = Kalkulator()
    okno.show()
    sys.exit(app.exec_())
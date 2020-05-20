from PySide2.QtWidgets import *
import random

class CycleISEN(QWidget):

    def __init__(self):
        QWidget.__init__(self)

        self.setWindowTitle("Cycles de l'ISEN Yncréa Ouest")
        self.setMinimumSize(500,300)

        self.layout = QVBoxLayout()

        self.text = QLabel()
        self.layout.addWidget(self.text)

        self.button = QPushButton("Changer le cycle")
        self.layout.addWidget(self.button)
        self.button.clicked.connect(self.buttonclicked)

        self.setLayout(self.layout)

    def buttonclicked(self):

        cycle = ['CSI','CIR','BIOST','CENT','BIAST','EST']
        self.text.setText(random.choice(cycle))


if __name__ == "__main__":
    app = QApplication([])
    win = CycleISEN()
    win.show()
    app.exec_()






from PySide2.QtWidgets import *

class Widget(QWidget):

    def __init__(self):
        QWidget.__init__(self)

        self.setWindowTitle("IHM")
        self.setMinimumSize(300,100)

        self.layout = QVBoxLayout()

        self.clic = 0
        self.button = QPushButton("Changer mon texte!")
        self.layout.addWidget(self.button)

        self.button.clicked.connect(self.buttonClosed)

        self.text = QTextEdit("Le nombre de clics va être affiché ici")
        self.layout.addWidget(self.text)

        self.setLayout(self.layout)

    def buttonClosed(self):

        self.clic += 1
        self.button.setText("Clic" + " " + str(self.clic))
        self.text.setText("Clic" + " " + str(self.clic))

if __name__ == "__main__":
    app = QApplication([])
    win = Widget()
    win.show()
    app.exec_()

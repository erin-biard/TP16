from PySide2.QtWidgets import *

class Widget(QWidget):

    def __init__(self):
        QWidget.__init__(self)

        self.setWindowTitle("IHM")

        self.layout = QHBoxLayout()

        self.progressBar = QProgressBar()
        self.layout.addWidget(self.progressBar)

        self.slider = QSlider()
        self.layout.addWidget(self.slider)
        self.slider.valueChanged.connect(self.progress)

        self.setLayout(self.layout)

    def progress(self,value):

        self.progressBar.setValue(value)

if __name__ == "__main__":
    app = QApplication([])
    win = Widget()
    win.show()
    app.exec_()

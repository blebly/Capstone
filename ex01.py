import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton

class Exam(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        btn = QPushButton('click', self)
        btn.resize(btn.sizeHint())
        btn.setToolTip('explanation <b>Hooray<b/>')
        btn.move(20,30)

        self.setGeometry(300,300,400,500)
        self.setWindowTitle('The first class')
        self.show()

app = QApplication(sys.argv)
w = Exam()
sys.exit(app.exec_())
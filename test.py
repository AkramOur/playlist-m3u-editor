import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget

app = QApplication(sys.argv)

root = QWidget()

root.show()

sys.exit(app.exec_())


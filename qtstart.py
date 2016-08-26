import sys
from PyQt4 import QtGui

app = QtGui.QApplication(sys.argv)

window = QtGui.QMainWindow()
window.setGeometry(100, 100, 500, 300)
window.setWindowTitle("PyQT Tuts!")
window.show()

sys.exit(app.exec_())
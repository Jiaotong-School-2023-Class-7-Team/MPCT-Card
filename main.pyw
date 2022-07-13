# -*- coding: utf-8 -*-

import sys
from MainWindow import *
import resourse
import ctypes
import setproctitle

resourse.qInitResources()
app = QtWidgets.QApplication(sys.argv)
app.setStyle("Fusion")
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID("MPCTCards")
setproctitle.setproctitle("MPCT Cards")
MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)
MainWindow.show()
bgMusic.start()
app.exec()

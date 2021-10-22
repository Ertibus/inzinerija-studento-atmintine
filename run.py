#!/usr/bin/env python3

import sys
from PyQt5.QtWidgets import QApplication
from program.index import PyQtGUI
from program.repo import *

if __name__ == '__main__':
    # Connect repositories
    Repository.connect("sqlite.db")

    # Draw window
    app = QApplication(sys.argv)
    ex = PyQtGUI()
    sys.exit(app.exec_())

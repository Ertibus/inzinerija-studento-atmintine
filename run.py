#!/usr/bin/env python3
import sys
from PyQt5.QtWidgets import QApplication
from program.index import PyQtGUI
from program.repo import *
import program.notifyd
import threading

DB_NAME = "data.sqlite"

if __name__ == '__main__':
    # Connect repositories
    NewRepository.connect(DB_NAME)

    # Notify
    notify_thread = threading.Thread(target=program.notifyd.work)
    notify_thread.run()

if False:
    # Draw window
    app = QApplication(sys.argv)
    ex = PyQtGUI()
    sys.exit(app.exec_())

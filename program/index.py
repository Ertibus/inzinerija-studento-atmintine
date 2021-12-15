from PyQt5 import QtCore
from PyQt5.QtWidgets import *
from program.ui import *

WINDOW_START_X = 200
WINDOW_START_Y = 100
WINDOW_SIZE_X = 800
WINDOW_SIZE_Y = 600


class PyQtGUI(QWidget):
    def __init__(self, ):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.layout = QVBoxLayout()

        with open("dark-mode.css") as file:
            self.setStyleSheet(file.read())

        self.navigator(0)

        self.setLayout(self.layout)
        self.setWindowTitle("PSI. Studento Atmintine")
        self.setGeometry(WINDOW_START_X, WINDOW_START_Y, WINDOW_SIZE_X, WINDOW_SIZE_Y)
        self.show()

    def navigator(self, message):
        if message == Message.login:
            self.clear_layout(self.layout)
            Login(self.layout, self.navigator)
        elif message == Message.home:
            self.clear_layout(self.layout)
            Home(self.layout, self.navigator)
        elif message == Message.new_event:
            self.clear_layout(self.layout)
            NewEvent(self.layout, self.navigator)
        elif message == Message.settings:
            self.clear_layout(self.layout)
        elif message == Message.forgot:
            self.clear_layout(self.layout)
            Recovery(self.layout, self.navigator)
        elif message == Message.clear:
            self.clear_layout(self.layout)
        pass

    def clear_layout(self, layout):
        while layout.count():
            child = layout.takeAt(0)
            if child.widget() is not None:
                child.widget().deleteLater()
            elif child.layout() is not None:
                self.clear_layout(child.layout())

from PyQt5.QtWidgets import *
from program.ui import Message

class Home():
    def __init__(self, body: QLayout, navigator):
        self.navigator = navigator
        self.body = body
        self.init_ui()

    def init_ui(self):
        wrapper = QVBoxLayout()
        self.body.addLayout(wrapper)

        wrapper.addWidget(QLabel("Hello World"))

from PyQt5.QtWidgets import *
from program.ui import Message

class Home():
    def __init__(self, body: QLayout, navigator):
        self.navigator = navigator
        self.body = body
        self.init_ui()

    def init_ui(self):
        wrapper = QGridLayout()
        wrapper.setColumnStretch(1, 1)
        self.body.addLayout(wrapper)

        button_layout = QVBoxLayout()

        btn_other = QPushButton("other")
        button_layout.addWidget(btn_other)

        button_layout.addStretch()

        btn_quit = QPushButton("Quit")
        button_layout.addWidget(btn_quit)

        event_layout = QVBoxLayout()
        event_layout.addWidget(QLabel("Hello there traveler!"))
        event_layout.addStretch()


        button_box = QGroupBox(" ")
        button_box.setLayout(button_layout)

        event_box = QGroupBox(" ")
        event_box.setLayout(event_layout)

        wrapper.addWidget(button_box, 0, 0, 1, 1)
        wrapper.addWidget(event_box, 0, 1, 1, 1)

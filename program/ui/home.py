from PyQt5.QtWidgets import *
from program.ui import Message
from datetime import datetime
from PyQt5.QtCore import Qt
import sys

class Home():
    def __init__(self, body: QLayout, navigator):
        self.navigator = navigator
        self.body = body
        self.init_ui()

    def init_ui(self):
        def _new():
            self.navigator(Message.new_event)

        def _exit():
            sys.exit(0)
            print("Exit")

        wrapper = QGridLayout()
        wrapper.setColumnStretch(1, 1)
        self.body.addLayout(wrapper)

        button_layout = QVBoxLayout()

        #
        btn_new = QPushButton("New")
        btn_new.clicked.connect(_new)
        button_layout.addWidget(btn_new)
        button_layout.addStretch()

        btn_quit = QPushButton("Quit")
        btn_quit.clicked.connect(_exit)
        button_layout.addWidget(btn_quit)
        #

        scroll = QScrollArea()
        event_layout = QVBoxLayout()

        # TODO Get entries from db
        event_layout.addWidget(TrackedEvent(
            "Test",
            "Case aaaaaaaaaaaaaaaa bbbbbbbbbbbbbb ccccccccccccccccc eeeeeeeeeeeeeee ddddddddd eeeeeeeeeee aaaaaaaaaa ssssssssssssd ddddddd",
            datetime.now().strftime("%Y-%m-%d")
        ).get_widget())

        event_layout.addWidget(TrackedEvent(
            "Test",
            "Case aaaaaaaaaaaaaaaa bbbbbbbbbbbbbb ccccccccccccccccc eeeeeeeeeeeeeee ddddddddd eeeeeeeeeee aaaaaaaaaa ssssssssssssd ddddddd",
            datetime.now().strftime("%Y-%m-%d")
        ).get_widget())
        event_layout.addStretch()


        button_box = QGroupBox()
        button_box.setLayout(button_layout)

        event_box = QWidget()
        event_box.setLayout(event_layout)

        scroll.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        scroll.setWidgetResizable(True)
        scroll.setWidget(event_box)

        wrapper.addWidget(button_box, 0, 0, 1, 1)
        wrapper.addWidget(scroll, 0, 1, 1, 1)


class TrackedEvent():
    def __init__(self, title: str, description: str, deadline: str):
        self.title = title
        self.description = description
        self.deadline = deadline


    def get_widget(self,):
        def _copy():
            pass


        def _edit():
            pass


        def _delete():
            pass


        widget_layout = QHBoxLayout()

        lbl_title = QLabel(self.title.upper())
        lbl_title.setStyleSheet("font-weight: bold")
        widget_layout.addWidget(lbl_title)

        #widget_layout.addWidget(QLabel(self.description))
        widget_layout.addStretch()
        widget_layout.addWidget(QLabel(f"Deadline: {self.deadline}"))

        # [ Buttons ]

        btn_copy = QPushButton("C")
        btn_copy.setFixedWidth(32)
        # TODO btn_copy.clicked.connect(EVENT)
        widget_layout.addWidget(btn_copy)
        btn_edit = QPushButton("E")
        btn_edit.setFixedWidth(32)
        # TODO btn_edit.clicked.connect(EVENT)
        widget_layout.addWidget(btn_edit)
        btn_delete = QPushButton("D")
        btn_delete.setFixedWidth(32)
        # TODO btn_delete.clicked.connect(EVENT)
        widget_layout.addWidget(btn_delete)

        lay = QVBoxLayout()
        lay.addLayout(widget_layout)
        desc = QLabel(self.description)
        desc.setStyleSheet("color: #666666")
        desc.setWordWrap(True)
        lay.addWidget(desc)

        btn_box = QGroupBox()
        btn_box.setLayout(lay)

        return btn_box

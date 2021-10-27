from PyQt5 import QtCore
from PyQt5.QtWidgets import *

from program.repo import Repository
from program.ui.message import Message

class NewEvent():
    def __init__(self, root, listener):
        self.root = root
        self.listener = listener
        self.init_ui()

    def init_ui(self):
        def _submit():
            try:
                pass
                # TODO Register user
                #FileMG.register_user(user_ent.text(), password)
            except Exception as err:
                print(err)
                QMessageBox.critical(None, "Error", str(err))

        def _back():
            self.listener(Message.home)

        main_layout = QGridLayout()
        self.root.addLayout(main_layout)

        main_layout.setRowStretch(0, 1)
        main_layout.setRowStretch(10, 1)
        main_layout.setColumnStretch(0, 1)
        main_layout.setColumnStretch(2, 1)

        title_lbl = QLabel("Title:")
        main_layout.addWidget(title_lbl, 1, 1)
        title_ent = QLineEdit()
        main_layout.addWidget(title_ent, 2, 1)

        desc_lbl = QLabel("Description:")
        main_layout.addWidget(desc_lbl, 3, 1)
        desc_ent = QLineEdit()
        main_layout.addWidget(desc_ent, 4, 1)

        deadline_lbl = QLabel("Deadline:")
        main_layout.addWidget(deadline_lbl, 5, 1)
        deadline_ent = QDateTimeEdit()
        main_layout.addWidget(deadline_ent, 6, 1)

        break_lbl = QLabel("    ")
        main_layout.addWidget(break_lbl, 7, 1)

        submit_btn = QPushButton("Submit")
        submit_btn.clicked.connect(_submit)
        main_layout.addWidget(submit_btn, 8, 1)

        back_btn = QPushButton("Back")
        back_btn.clicked.connect(_back)
        main_layout.addWidget(back_btn, 9, 1)

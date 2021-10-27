#!/usr/bin/env python3
from PyQt5 import QtCore
from PyQt5.QtWidgets import *

from program.ui.message import Message

class Login():
    def __init__(self, root, listener, new_user):
        self.root = root
        self.listener = listener
        self.new_user = new_user
        self.init_ui()

    def press_login(self, user:str, password:str):
        try:
            pass
            # TODO login check
            #FileMG.login_user(user, password)
        except Exception as err:
            QMessageBox.critical(None, "Error", str(err))
            print(err)
        else:
            self.listener(Message.home)

    #0   1              2
    #    +-------------+
    #1   | User:       |
    #2   | [         ] |
    #3   | Password:   |
    #4   | [         ] |
    #5   | Password:   |
    #6   | [         ] |
    #7   |             |
    #8   |  {SUBMIT}   |
    #    +-------------+
    #10
    def press_register(self):
        def _submit():
            try:
                password = password_ent.text()
                if password != cpassword_ent.text():
                    raise ValueError("Passwords Don't Match")
                # TODO Register user
                #FileMG.register_user(user_ent.text(), password)
            except Exception as err:
                print(err)
                QMessageBox.critical(None, "Error", str(err))
            self.listener(Message.clear)
            self.init_ui()

        main_layout = QGridLayout()
        self.root.addLayout(main_layout)

        main_layout.setRowStretch(0, 1)
        main_layout.setRowStretch(10, 1)
        main_layout.setColumnStretch(0, 1)
        main_layout.setColumnStretch(2, 1)

        user_lbl = QLabel("User:")
        main_layout.addWidget(user_lbl, 1, 1)
        user_ent = QLineEdit()
        main_layout.addWidget(user_ent, 2, 1)

        password_lbl = QLabel("Password:")
        main_layout.addWidget(password_lbl, 3, 1)
        password_ent = QLineEdit()
        password_ent.setEchoMode(QLineEdit.Password)
        main_layout.addWidget(password_ent, 4, 1)

        password_lbl = QLabel("Confirm Password:")
        main_layout.addWidget(password_lbl, 5, 1)
        cpassword_ent = QLineEdit()
        cpassword_ent.setEchoMode(QLineEdit.Password)
        main_layout.addWidget(cpassword_ent, 6, 1)

        break_lbl = QLabel("    ")
        main_layout.addWidget(break_lbl, 7, 1)

        submit_btn = QPushButton("Submit")
        submit_btn.clicked.connect(_submit)
        main_layout.addWidget(submit_btn, 8, 1)


    #0   1              2
    #    +-------------+
    #1   | User:       |
    #2   | [         ] |
    #3   | Password:   |
    #4   | [         ] |
    #5   |             |
    #6   |   {LOGIN}   |
    #    +-------------+
    #7
    def init_ui(self):
        def _login():
            self.press_login(user_ent.text(), password_ent.text())

        def _register():
            self.press_register()

        if self.new_user == True:
            self.new_user = False
            _register()
            return

        main_layout = QGridLayout()
        self.root.addLayout(main_layout)

        main_layout.setRowStretch(0, 1)
        main_layout.setRowStretch(10, 1)
        main_layout.setColumnStretch(0, 1)
        main_layout.setColumnStretch(2, 1)

        user_lbl = QLabel("User:")
        main_layout.addWidget(user_lbl, 1, 1)
        user_ent = QLineEdit()
        main_layout.addWidget(user_ent, 2, 1)

        password_lbl = QLabel("Password:")
        main_layout.addWidget(password_lbl, 3, 1)
        password_ent = QLineEdit()
        password_ent.setEchoMode(QLineEdit.Password)
        main_layout.addWidget(password_ent, 4, 1)

        break_lbl = QLabel("    ")
        main_layout.addWidget(break_lbl, 5, 1)

        login_btn = QPushButton("Login")
        login_btn.clicked.connect(_login)
        main_layout.addWidget(login_btn, 6, 1)

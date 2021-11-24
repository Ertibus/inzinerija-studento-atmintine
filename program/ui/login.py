#!/usr/bin/env python3
from PyQt5 import QtCore
from PyQt5.QtWidgets import *

from program.ui.message import Message
from program.repo import NewRepository
from program.ui.recovery_questions import question_list

class Login():
    def __init__(self, root, listener):
        self.root = root
        self.listener = listener
        self.init_ui()

    def press_login(self, user:str, password:str):
        try:
            NewRepository.login(user, password)
            pass
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
                NewRepository.add_user(user_ent.text(), password, combo_box.currentIndex(), awnser.text())
            except Exception as err:
                print(err)
                QMessageBox.critical(None, "Error", str(err))
            self.listener(Message.clear)
            self.init_ui()

        main_layout = QGridLayout()
        self.root.addLayout(main_layout)

        main_layout.setRowStretch(0, 1)
        main_layout.setRowStretch(100, 1)
        main_layout.setColumnStretch(0, 1)
        main_layout.setColumnStretch(1, 1)
        main_layout.setColumnStretch(2, 1)

        register_layout = QVBoxLayout()
        user_lbl = QLabel("User:")
        register_layout.addWidget(user_lbl)
        user_ent = QLineEdit()
        register_layout.addWidget(user_ent)

        password_lbl = QLabel("Password:")
        register_layout.addWidget(password_lbl)
        password_ent = QLineEdit()
        password_ent.setEchoMode(QLineEdit.Password)
        register_layout.addWidget(password_ent)

        password_lbl = QLabel("Confirm Password:")
        register_layout.addWidget(password_lbl)
        cpassword_ent = QLineEdit()
        cpassword_ent.setEchoMode(QLineEdit.Password)
        register_layout.addWidget(cpassword_ent)

        rbox = QGroupBox("User Info")
        rbox.setLayout(register_layout)
        main_layout.addWidget(rbox, 1, 1)

        sec_layout = QVBoxLayout()
        combo_lbl = QLabel("Question:")
        sec_layout.addWidget(combo_lbl)

        combo_box = QComboBox()
        for combo in question_list:
            pass
        combo_box.addItem("The name of your first pet")
        combo_box.addItem("City you were born in")
        combo_box.addItem("Favorite movie")
        sec_layout.addWidget(combo_box)

        answer_lbl = QLabel("Answer:")
        sec_layout.addWidget(answer_lbl)
        awnser = QLineEdit()
        sec_layout.addWidget(awnser)

        recovery_group = QGroupBox("User Recovery")
        recovery_group.setLayout(sec_layout)
        main_layout.addWidget(recovery_group, 2, 1)

        submit_btn = QPushButton("Submit")
        submit_btn.clicked.connect(_submit)
        main_layout.addWidget(submit_btn, 90, 1)



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

        def _forgot():
            self.listener(Message.forgot)


        if NewRepository.user_exists() == False:
            _register()
            return

        main_layout = QGridLayout()
        self.root.addLayout(main_layout)

        main_layout.setRowStretch(0, 1)
        main_layout.setRowStretch(10, 1)
        main_layout.setColumnStretch(0, 1)
        main_layout.setColumnStretch(1, 1)
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

        forgot_btn = QPushButton("I forgot my password")
        forgot_btn.clicked.connect(_forgot)
        main_layout.addWidget(forgot_btn, 7, 1)

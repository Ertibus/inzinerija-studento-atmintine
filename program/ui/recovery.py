
from PyQt5 import QtCore
from PyQt5.QtWidgets import *

from program.ui.message import Message
from program.repo import NewRepository
from program.ui.recovery_questions import question_list

class Recovery():
    def __init__(self, root, listener):
        self.root = root
        self.listener = listener
        self.show_password()

    def show_password(self):
        def _submit():
            try:
                if (s_answer == answer.text()):
                    QMessageBox.information(None, "Password", "Password: {}".format(s_pass))
                else:
                    raise ValueError("Security question or awnser does not match!")

            except Exception as err:
                print(err)
                QMessageBox.critical(None, "Error", str(err))

        def _back():
            self.listener(Message.login)


        (s_question_id, s_answer, s_pass) = NewRepository.get_recovery_info()
        main_layout = QGridLayout()
        self.root.addLayout(main_layout)

        main_layout.setRowStretch(0, 1)
        main_layout.setRowStretch(100, 1)
        main_layout.setColumnStretch(0, 1)
        main_layout.setColumnStretch(1, 1)
        main_layout.setColumnStretch(2, 1)

        sec_layout = QVBoxLayout()
        combo_lbl = QLabel("Question:")
        sec_layout.addWidget(combo_lbl)
        combo_box = QLineEdit()
        combo_box.setText(question_list[s_question_id])
        combo_box.setReadOnly(True)
        sec_layout.addWidget(combo_box)

        answer_lbl = QLabel("Answer:")
        sec_layout.addWidget(answer_lbl)
        answer = QLineEdit()
        sec_layout.addWidget(answer)

        break_lbl = QLabel("    ")
        main_layout.addWidget(break_lbl, 5, 1)

        main_layout.addLayout(sec_layout, 1, 1)
        submit_btn = QPushButton("Submit")
        submit_btn.clicked.connect(_submit)
        main_layout.addWidget(submit_btn, 90, 1)

        back_btn = QPushButton("Back")
        back_btn.clicked.connect(_back)
        main_layout.addWidget(back_btn, 91, 1)

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget,  QPushButton, QHBoxLayout,QVBoxLayout, QLabel, QMessageBox, QRadioButton
 
app = QApplication([])

main_window = QWidget()
main_window.setWindowTitle("Конкурс від Crazy People")
main_window.resize(400, 200)

lb_question = QLabel ("В якому році канал отримав золоту кнопку?")
rb_answer_1 = QRadioButton("2010")
rb_answer_2 = QRadioButton("2005")
rb_answer_3 = QRadioButton("2015")
rb_answer_4 = QRadioButton("2020")

layout_main = QVBoxLayout()
layoutH1 = QHBoxLayout()
layoutH2 = QHBoxLayout()
layoutH3 = QHBoxLayout()
layoutH1.addWidget(lb_question, alignment = Qt.AlignCenter)
layoutH2.addWidget(rb_answer_1, alignment = Qt.AlignCenter)
layoutH2.addWidget(rb_answer_2, alignment = Qt.AlignCenter)
layoutH3.addWidget(rb_answer_3, alignment = Qt.AlignCenter)
layoutH3.addWidget(rb_answer_4, alignment = Qt.AlignCenter)

layout_main.addLayout(layoutH1)
layout_main.addLayout(layoutH2)
layout_main.addLayout(layoutH3)
main_window.setLayout(layout_main)


def show_win():
    victory_window = QMessageBox()
    victory_window.setText("Вірно!")
    victory_window.exec_()

def show_lose():
    lose_window = QMessageBox()
    lose_window.setText("Не вірно!")
    lose_window.exec_()
    
rb_answer_1.clicked.connect(show_lose)
rb_answer_2.clicked.connect(show_win)
rb_answer_3.clicked.connect(show_lose)
rb_answer_4.clicked.connect(show_lose)

main_window.show()

app.exec_()
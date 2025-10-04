import sys
from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QLabel,
    QPushButton,
    QVBoxLayout,
    QHBoxLayout,
)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFontDatabase
from wordlist import word_pairs
import random


class Flashcard(QWidget):
    def __init__(self):
        super().__init__()

        font_id = QFontDatabase.addApplicationFont(
            "Python Projects/Teko-VariableFont_wght.ttf"
        )
        self.font_family = QFontDatabase.applicationFontFamilies(font_id)[0]

        self.setWindowTitle("Flashcard")
        self.setFixedSize(600, 425)
        self.word_label = QLabel("Label")
        self.translate_button = QPushButton("Translate")
        self.next_button = QPushButton("Next")
        self.current_word = ("")
        self.translate_counter = 0
        self.initUI()

    def initUI(self):
        main_layout = QVBoxLayout()
        self.setLayout(main_layout)
        main_layout.addWidget(self.word_label)
        button_layout = QHBoxLayout()
        button_layout.addWidget(self.translate_button)
        button_layout.addWidget(self.next_button)
        main_layout.addLayout(button_layout)

        self.word_label.setStyleSheet(
            "background-color: hsl(187, 82%, 56%);"
            f"font-family: '{self.font_family}';"
            "font-size: 100px;"
            "border: 3px solid #444;"
            "border-radius: 15px;"
        )
        self.word_label.setFixedHeight(250)
        self.word_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.setStyleSheet(
            "QPushButton{"
            "font-size: 60px;"
            "background-color: hsl(174, 75%, 80%);"
            f"font-family: '{self.font_family}';"
            "border: 3px solid #444;"
            "border-radius: 15px;"
            "}"

            "QPushButton:hover{"
            "background-color: hsl(174, 75%, 60%);""}"
        )
        
        self.translate_button.setFixedHeight(125)
        self.next_button.setFixedHeight(125)

        self.current_word = random.choice(word_pairs)
        self.word_label.setText(self.current_word[0])

        self.translate_button.clicked.connect(self.translate)  
        self.next_button.clicked.connect(self.next)
        
    def translate(self):
        if self.translate_counter == 0:
            self.word_label.setText(self.current_word[1])
            self.translate_counter = 1
        elif self.translate_counter == 1:
            self.word_label.setText(self.current_word[0])
            self.translate_counter = 0
    def next(self):
        self.current_word = random.choice(word_pairs)
        self.word_label.setText(self.current_word[0])
        self.translate_counter = 0


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Flashcard()
    window.show()
    sys.exit(app.exec_())

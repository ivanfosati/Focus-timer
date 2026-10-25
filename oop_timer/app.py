import sys
import clock
from PySide6.QtCore import Qt, QSize, Slot
from PySide6.QtWidgets import (QApplication, QLabel, QMainWindow, 
                               QHBoxLayout, QVBoxLayout, QPushButton, QWidget)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Set settings for the window #
        self.setWindowTitle("Pomodoro Timer")
        self.setFixedSize(QSize(500,650))

        MainLayout = QHBoxLayout()

        self.button = QPushButton("Click")
        self.button.clicked.connect(self.say_hello) 


        MainLayout.addWidget(self.button)

        widget = QWidget()
        widget.setLayout(MainLayout)

        self.setCentralWidget(widget)

    @Slot()
    def say_hello(self):
        print("Button clicked")



if __name__ == "__main__":
    app = QApplication([])

    window = MainWindow()

    window.show()

    app.exec()



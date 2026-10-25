import sys
from timer import Clock
import time
from PySide6.QtCore import Slot, QSize, QTimer, QTime, Qt
from PySide6.QtWidgets import (QApplication, 
                               QLabel,
                               QPushButton, 
                               QWidget, 
                               QMainWindow, 
                               QHBoxLayout, 
                               QVBoxLayout, 
                               QLineEdit)

clock = Clock()

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        # Set settings for the window #
        self.setWindowTitle("Pomodoro Timer")
        self.setFixedSize(QSize(600,400))

        # Define Layouts and properties #
        main_layout    = QVBoxLayout()
        buttons_layout = QHBoxLayout()

        main_layout.setContentsMargins(0,0,0,0)
        main_layout.setSpacing(20)
        
        # Define widgets for the app
        self.start_button = QPushButton("Start timer")

        # Signals and Slots #
        self.start_button.clicked.connect(self.startClock)
        self.line = QLineEdit()
        save_button = QPushButton("Save")

        ## Testing ##
        self.label = QLabel(self)
        

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.show_time)
        self.timer.start(1000)

        # Add Widgets #
        ### Buttons layout ###
        buttons_layout.addWidget(self.line)
        buttons_layout.addWidget(save_button)

        ### Main layout ###
        main_layout.addWidget(self.label)
        main_layout.addLayout(buttons_layout)
        main_layout.addWidget(self.line)
        main_layout.addWidget(self.start_button)


        widget = QWidget()
        widget.setLayout(main_layout)
        
        self.setCentralWidget(widget)

    @Slot()
    def show_time(self):
        pass
        #time = QTime.currentTime()
        #self.label.setText(text))


    @Slot()
    def startClock(self):
        userInput = self.line.text()
        if (userInput == ""):
            print("Ingrese una etiqueta")
        else:
            clock.run(userInput, 3)

        self.line.clear()
    
if __name__ == "__main__":
    app = QApplication(sys.argv)

    label = QLabel()
    s_label = QLabel()
    label.setAlignment(Qt.AlignmentFlag.AlignCenter)
    label.setStyleSheet(
            """font-weight: bold; 
            font-size: 22px; 
            width: 25px; 
            height: 25px;""")

    s_label.setStyleSheet(
            """font-weight: bold; 
            font-size: 16px; 
            width: 25px; 
            height: 25px""")

    start_clock = time.monotonic()

    def timerEvent():
        elapsed = time.monotonic() - start_clock


        if elapsed < 10:
            label.setText("Time: {:0.2f}".format(elapsed))
        else:
            label.setText("Tiempo terminado")
        

    timer = QTimer()
    timer.timeout.connect(timerEvent)
    label.show()
    timer.start(1000)

    app.exec() 

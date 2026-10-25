import sys
from clock import Clock
from PySide6.QtCore import Qt, QSize, Slot, QTimer
from PySide6.QtWidgets import (QApplication, QLabel, QMainWindow, 
                               QHBoxLayout, QVBoxLayout, QPushButton, 
                               QWidget)

clock = Clock()

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.height = 650
        self.width  = 500

        # Settings for the window #
        self.setWindowTitle("Pomodoro Timer")
        self.setFixedSize(QSize(self.width, self.height))

        mainLayout = QVBoxLayout()

        ## Define buttons ##
        self.StartButton = QPushButton("Start timer")
        self.StartButton.clicked.connect(clock.start) 
        self.PauseButton = QPushButton("Pause timer")
        self.PauseButton.clicked.connect(clock.pause) 

        ## Set Label for time display ##
        self.timeLabel = QLabel()
        self.timeLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.timeLabel.setStyleSheet(
            """
            font-weight: bold; 
            font-size:   24px; 
            width:       25px; 
            height:      25px;
            """)


        mainLayout.addWidget(self.timeLabel)
        mainLayout.addWidget(self.StartButton)
        mainLayout.addWidget(self.PauseButton)

        widget = QWidget()
        widget.setLayout(mainLayout)

        self.setCentralWidget(widget)

    @staticmethod
    def format_time():
        min, sec    = divmod(clock.show_time(), 60)
        hour, min   = divmod(min, 60)
        return '%02d:%02d:%02d' % (hour, min, sec)

    def displayTime(self):
        print(clock.isRunning)
        if clock.isRunning: 
            self.timeLabel.setText(self.format_time())
        else:
            self.timeLabel.setText("--:--:--")

    def Button():
        pass

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()

    qtimer = QTimer()
    qtimer.timeout.connect(window.displayTime)
    qtimer.start(1000)

    window.show()
    sys.exit(app.exec())




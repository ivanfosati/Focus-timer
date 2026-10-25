import sys
from PySide6.QtWidgets import (QApplication, QLabel)
import time
import timer 
from PySide6.QtCore import QTimer, Qt


    
if __name__ == "__main__":
    app = QApplication(sys.argv)

    label = QLabel()
    s_label = QLabel()
    label.setAlignment(Qt.AlignmentFlag.AlignCenter)
    label.setStyleSheet(
            "font-weight: bold; font-size: 22px; width: 25px; height: 25px;"
                )
    s_label.setStyleSheet(
            "font-weight: bold; font-size: 16px; width: 25px; height: 25px;"
                )
    start_clock = time.monotonic()
    def timerEvent():
        elapsed = time.monotonic() - start_clock


        if elapsed < 10:
            label.setText(str(elapsed))
        else:
            label.setText("Tiempo terminado")
        
        

    timer = QTimer()
    timer.timeout.connect(timerEvent)
    label.show()
    timer.start(1000)

    app.exec() 


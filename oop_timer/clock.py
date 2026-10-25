#!/usr/bin/env python

import time

class Clock():
    def __init__(self):
        self.isRunning   = False

        self.start_timer = 0
        self.pause_timer = 0

    def start(self):
        if not self.isRunning:
            self.isRunning = True
            print("Iniciando timer...\n")
            self.start_timer = time.monotonic() # Start clock

    def pause(self):
        if self.isRunning: 
            self.isRunning = False
            print("Pausa\n")
            self.pause_timer = time.monotonic()
    

    def show_time(self):
#        elapsed = self.pause_timer - self.start_timer
#        print("Tiempo: {:0.2f}\n".format(elapsed))
        elapsed = time.monotonic() - self.start_timer
#        print("Testeo: {:0.2f}\n".format(elapsed))
        return elapsed

### Debugging ###
    
if __name__ == "__main__":
    clock = Clock()
    clock.start()
    time.sleep(5)
    clock.show_time()
    print(clock.show_time())

    clock.pause()

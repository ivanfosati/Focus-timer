#!/usr/bin/env python

import time

class Clock():
    def __init__(self, duration):
        self.duration    = duration
        self.isRunning   = False

        self.start_timer = 0
        self.pause_timer = 0

    def start(self):
        if not self.isRunning:
            print("Iniciando timer...\n")
            self.start_timer = time.monotonic() # Start clock
            self.isRunning = True

    def pause(self):
        if self.isRunning: 
            print("Pausa\n")
            self.pause_timer = time.monotonic()
            self.isRunning = False
    

    def show_time(self):
        elapsed = self.pause_timer - self.start_timer
        print("Tiempo: {:0.2f}\n".format(elapsed))


### Debugging ###

#t = 5
#clock = Clock(t)
#clock.start()
#
#time.sleep(t)
#
#clock.pause()
#clock.show_time()

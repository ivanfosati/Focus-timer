#!/usr/bin/env python3
import time
import database

class Clock:
    def __init__(self,label, _duration):
        self.label    = label
        self.duration = _duration
        database.createTable()
    
    # decorator for the timer
    def set_label(base_fn):
        def add_label(self):
            if self.label == "study":
                print("Studying...")
            elif self.label == "break":
                print("Take your time")
            base_fn(self)
        return add_label

    # functions should handle one task!
    @set_label # decorator 
    def timer(self):
        start_time = time.time()
        final_time = start_time + self.duration + 1

        while time.time() <= final_time:

            elapsed_time = time.time() - start_time
            print(int(elapsed_time), end='\r', flush=True)
            time.sleep(1)

        return start_time, final_time, self.label, elapsed_time

    # Funcion que tome los datos y los guarde en database.py

    def saveData(self):
        starTime, finalTime, dt, label = self.timer() 
        database.addElements(starTime, finalTime, dt, label)

def main():
    while True:
        try:
            userInput = input("Qué vas a hacer hoy?")

            if userInput == "stats":
                clock = Clock(x,y)
                clock.saveData()
            else:
                timeInput = int(input("Time:"))
                label = input("mode: ")
                clock = Clock(label, timeInput)
                clock.timer()

            

        except KeyboardInterrupt:
            print("\nProgram terminated by user.")
            #
            # Clean-up and save data just in case.
            #
            break
        except ValueError:
            print("Ingrese otro número.")



if __name__ == "__main__":
    main()

#!/usr/bin/env python3
import time
import database
from datetime import datetime
import subprocess

class Clock:
    def __init__(self):
        database.createTable()

### Check dataclasses para devolver mejor los valores de una funcion
### sería: Studen: name:str, marks: int -> func(): return Student("Fulano", 100)
    def timer(self, label, duration):
        startTimer = time.time()
        endTimer = startTimer + duration
        # Format times for database
        formatted_stimer = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(startTimer))
        formatted_etimer = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(endTimer))

        while True:
            if time.time() >= endTimer:
                break
            elapsed_time = (time.time() - startTimer)
            print(elapsed_time, end='\r', flush=True)
            time.sleep(0.5)

        return (formatted_stimer, 
                formatted_etimer, 
                label, 
                duration
                )

    # Funcion que tome los datos y los guarde en database.py
    def saveData(self, startTime, endTime, label, time):
        database.addElements(startTime, endTime, label, time)

    def run(self, label, duration):
        startTime, endTime, label, time = self.timer(label, duration)
        self.saveData(startTime, endTime, label, time)

        #subprocess.call("dunstify 'Sesión terminada'", shell=True)
        #subprocess.call("paplay '/usr/share/sounds/freedesktop/stereo/alarm-clock-elapsed.oga'", 
        #                shell=True)
    def showData(self):
        database.showTable()


def main():
    while True:
        try:
            clock = Clock()
            userInput = input("Qué vas a hacer hoy? (study, hobbie, break, testing, stats)\n")
            if userInput != "stats":
                t = int(input("Tiempo: "))
                clock.run(userInput, t)
            elif userInput == "stats":
                clock.showData()



        except KeyboardInterrupt:
            print("\nProgram terminated by user. Bye bye!")
            # To-Do
            # Clean-up and save data just in case.
            #
            break
        except ValueError:
            print("Ingrese otro número.")



if __name__ == "__main__":
    main()

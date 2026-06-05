#!/usr/bin/env python3
import time
import database
import subprocess

class Clock:
    def __init__(self):
        database.createTable()

    def timer(self, label, _duration):
        startTimer = time.time()
        endTimer = startTimer + _duration
        
        # Format times for database
        formatted_stimer = time.strftime("%Y-%m-%dT%H:%M:%S", time.localtime(startTimer))
        formatted_etimer= time.strftime("%Y-%m-%dT%H:%M:%S", time.localtime(endTimer))

        while time.time() <= endTimer:

            elapsed_time = time.time() - startTimer
            print(int(elapsed_time), end='\r', flush=True)
            time.sleep(1)

        return (formatted_stimer, 
                formatted_etimer, 
                label, 
                elapsed_time
                )

    # Funcion que tome los datos y los guarde en database.py

    def saveData(self, startTime, endTime, label, time):
        database.addElements(startTime, endTime, label, time)

    def run(self, label, _duration):
        startTime, endTime, label, time = self.timer(label, _duration)
        self.saveData(startTime, endTime, label, time)

        subprocess.call("dunstify 'Sesión terminada'", shell=True)
        subprocess.call("paplay '/usr/share/sounds/freedesktop/stereo/alarm-clock-elapsed.oga'", 
                        shell=True)
    def showData(self):
        database.showTable()


def main():
    while True:
        try:
            clock = Clock()
            userInput = input("Qué vas a hacer hoy? (study, break, stats)\n")

            if userInput == "study":
                t = int(input("Tiempo: "))
                clock.run("study", t)
            elif userInput == "break":
                b = int(input("Tiempo: "))
                clock.run("break", b)
            elif userInput == "stats":
                clock.showData()



        except KeyboardInterrupt:
            print("\nProgram terminated by user.")
            # To-Do
            # Clean-up and save data just in case.
            #
            break
        except ValueError:
            print("Ingrese otro número.")



if __name__ == "__main__":
    main()

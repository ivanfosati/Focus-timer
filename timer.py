#!/usr/bin/env python3
import time
from database import DataBase

#from datetime import datetime

        
def Timer(duration):
    start_time = time.time()            # Guarda el tiempo (en segundos) apenas la funcion es llamada
    final_time = start_time + duration + 1     # tiempo total de estudio + 1 seg. para redondeo
    t_inicial = time.gmtime(start_time)
    t_final   = time.gmtime(final_time)

    while time.time() <= final_time:
        elapsed_time = int(time.time() - start_time)  # time.time() devuelve nuevamente el tiempo 
        hours, remainder = divmod(elapsed_time, 3600) # y lo resta al primero que guardamos.
        mins, secs = divmod(remainder, 60)

        # Formato del tiempo #

        # print(f'Time: {time.strftime("%d-%m-%Y %H:%M:%S", time.localtime(start_time))}', end="\r")
        print(f'{hours:02d}:{mins:02d}:{secs:02d}', end="\r", flush=True) 
        time.sleep(1)


    return t_inicial, t_final, elapsed_time



class Manager:
    def __init__(self, duration, rest, sets):
        self.duration = duration
        self.rest = rest
        self.sets = sets

        self.queue = []
        self.planner(sets)

    def planner(self, sets):
        n_sets = (2 * sets) -1 
        i = 0
        # Crear orden de tareas
        for i in range(0, n_sets):
            if (i % 2 == 0):
                self.queue.insert(i, "study")
            else:
                self.queue.insert(i, "break")

        self.queue.append("end")
        
        return self.queue


    def show_time(self): 
        total_time = 0 

        for label in self.queue:
            if (label == "study"):
                print("Estudiando: ")
                Timer(self.duration)
                total_time += Timer(self.duration).elapsed_time
                print(f'Tiempo total de estudio: {total_time}')
                
            elif (label == "break"):
                print("Descansando: ")
                Timer(self.rest)
            
            else:
                print("Sesión finalizada. Felicidades!")
                break

        return total_time

    def hello(self):
        t_inicial = t_inicial.Timer(self.duration)
        t_final = t_final.Timer(self.duration)
        total_time = total_time.show_time(self)

        db = DataBase
        db.add_elements(self, t_inicial, t_final, total_time)


def main():
    while True:
        try:
            t = int(input("Timer: "))
            r = int(input("Rest: "))
            n = int(input("Sets: "))

            

            clock = Manager(t, r, n)
            clock.show_time()

        except ValueError:

            print("Ingrese otro número")
        
        
if __name__ == "__main__":
    main()

#!/usr/bin/env python3
import time
from datetime import datetime
import sqlite3

def timer(x):
    start_time = time.time()            # Guarda el tiempo (en segundos) apenas la funcion es llamada
    final_time = start_time + x + 1     # tiempo total de estudio + 1 seg. para redondeo
    t_inicial = time.gmtime(start_time).tm_hour

    while time.time() <= final_time:
        elapsed_time = int(time.time() - start_time)  # time.time() devuelve nuevamente el tiempo 
        hours, remainder = divmod(elapsed_time, 3600) # y lo resta al primero que guardamos.
        mins, secs = divmod(remainder, 60)
        ## Formato del tiempo #
        # print(f'Time: {time.strftime("%d-%m-%Y %H:%M:%S", time.localtime(start_time))}', end="\r")
        print(f'{hours:02d}:{mins:02d}:{secs:02d}', end="\r", flush=True) 
        time.sleep(1)

    return hours, mins, secs


 ### Divide las sesiones de estudio en sets ###

def sets(n, t, r):
    i = 1
    while i <= n:
        if i<n:
            print(f'Study: {timer(t)}', end='\r')
            print(f'Rest: {timer(r)}', end='\n')
            i += 1
            
        else:
            print(f'Study: {timer(t)}', end='\r')
            i += 1
        





def main():
    while True:
        try:
            n = int(input("# Sets: "))
            if n == 1:
                t = int(input("focus time: "))
                sets(n, t, 0)
            else:
                t = int(input("focus time: "))
                r = int(input("rest time: "))
                sets(n, t, r)
            

            if t < 0  or n <= 0:  
                raise ValueError

        except ValueError:
            print("Ingrese otro número")
        
        
if __name__ == "__main__":
    main()

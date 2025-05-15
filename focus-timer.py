#!/usr/bin/env python3
import time
import sys


def timer(x):
    start_time = time.time()            # Guarda el tiempo (en segundos) apenas la funcion es llamada                                           
    final_time = start_time + x + 1     # tiempo total de estudio + 1 seg. para redondeo

    while time.time() <= final_time:
        elapsed_time = int(time.time() - start_time) # time.time() devuelve nuevamente                                                                              el tiempo y lo resta al primero que guardamos
        hours, remainder = divmod(elapsed_time, 3600)
        mins, secs = divmod(remainder, 60)
        ## Formato del tiempo ##
        print(f'{hours:02d}:{mins:02d}:{secs:02d}', end="\r", flush=True) 
        time.sleep(1) 

def sets(n, t, r):                      # Divide las sesiones de estudio en "sets"
    for i in range(1, n+1):
        timer(t)                        #Comienza el temporizador
        print("Time Finish, Starting rest time in 5, 4, 3, 2, 1..")
        time.sleep(5)
        timer(r)                        #Comienza el descanso
        print("Rest time finished. Go back to work")

 

def main():
    while True:
        try:
            t = int(input("focus time: "))
            r = int(input("rest time: "))
            n = int(input("# Sets: "))
            
            if t < 0 or r < 0 or n <= 0:  
                raise ValueError
            sets(n, t, r)

        except ValueError:
            print("Ingrese otro número")
        
        
if __name__ == "__main__":
    main()

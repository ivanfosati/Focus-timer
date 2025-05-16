#!/usr/bin/python3

import curses
import time

def timer(stdscr, x):
    start_time = time.time()
    final_time = start_time + x + 1
    while time.time() <= final_time:
        elapsed_time = int(time.time() - start_time)
        hours, remainder = divmod(elapsed_time, 3600)
        mins, secs = divmod(remainder, 60)
        time_str = f'{hours:02d}:{mins:02d}:{secs:02d}'
        stdscr.addstr(5, 35, time_str)
        time.sleep(1)


def sets(stdscr, n, t, r):                      # Divide las sesiones de estudio en "sets"
    for i in range(1, n+1):
        timer(stdscr, t)                        #Comienza el temporizador
        stdscr.addstr("Time Finish, Starting rest time in 5, 4, 3, 2, 1..")
        time.sleep(5)
        timer(stdscr, r)                        #Comienza el descanso
        stdscr.addstr("Rest time finished. Go back to work")


def main(stdscr):
    curses.echo()
    data = []

    stdscr.clear()
    stdscr.addstr(10, 30, "Ingrese tiempo de concentracion: ")
    t = stdscr.getstr().decode('utf-8')
    stdscr.clear()
    stdscr.addstr(10, 32, "Ingrese tiempo de descanso: ")
    r = stdscr.getstr().decode('utf-8')
    stdscr.clear()
    stdscr.addstr(10, 34, "Ingrese cantidad de sets: ")
    n = stdscr.getstr().decode('utf-8')
    stdscr.clear()

    while True:
        try: 
            t = int(t)
            r = int(r)
            n = int(n)
            
            sets(stdscr, n, t, r)
        except ValueError:
            stdscr.addstr("ingrese otro numero")
            stdscr.refresh()

        return
        data = [t, r, n]

    stdscr.clear()
    stdscr.addstr(10, 10, f't = {data[0]}')
    stdscr.addstr(11, 10, f'r = {data[1]}')
    stdscr.addstr(12, 10, f'n = {data[2]}')
    stdscr.refresh()

    time.sleep(2)
curses.wrapper(main)

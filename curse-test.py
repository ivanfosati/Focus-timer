#!/usr/bin/python3

import curses

from time import strftime, sleep

#def main(stdscr):
#    curses.curs_set(0)  # Oculta el cursor
#    while True:
 #       stdscr.clear()
  #      time_str = strftime("%H:%M:%S")
   #     height, width = stdscr.getmaxyx()
    #    x = width//2 - len(time_str)//2
     ##   y = height//2
      #  stdscr.addstr(y, x, time_str, curses.A_BOLD)
#     stdscr.refresh()
     #   sleep(1)

#curses.wrapper(main)

###################################################################
def timer(x):
    start_time = time.time()                                                       
    final_time = start_time + x + 1    
    while time.time() <= final_time:
        elapsed_time = int(time.time() - start_time)         
        hours, remainder = divmod(elapsed_time, 3600)
        mins, secs = divmod(remainder, 60)
        ## Formato del tiempo ##
        print(f'{hours:02d}:{mins:02d}:{secs:02d}', end="\r", flush=True) 
        time.sleep(1) 

def sets(n, t, r):                          
    for i in range(1, n+1):
        timer(t)                        #Comienza el temporizador
        print("Time Finish, Starting rest time in 5, 4, 3, 2, 1..")
        time.sleep(5)
        timer(r)                        #Comienza el descanso
        print("Rest time finished. Go back to work")

def main(stdscr):
    curses.curs_set(0)
    curses.echo()
    while True:
        try:
            stdscr.clear()
            t = stdscr.getch()
            r = stdscr.getch()
            n = stdscr.getch()
            time_str = strftime("%H:%M:%S")
            height, width = stdscr.getmaxyx()
            x = width//2 - len(time_str)//2
            y = height//2
            stdscr.addstr(y, x, time_str, curses.A_BOLD)
            stdscr.refresh()
            sleep(1)
        except ValueError:
            print("Ingrese otro número")

curses.wrapper(main)

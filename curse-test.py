#!/usr/bin/python

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


def main(stdscr):
    while True:
        stdscr.clear()
        time_str = strftime("%H:%M:%S")
        height, width = stdscr.getmaxyx()
        stdscr.addstr(time_str)
        stdscr.refresh()
        sleep(1)

curses.wrapper(main)

#!/usr/bin/env python


import time
import pyglet


def alarm(hh, mm):
    check = True
    while check:
        curr_hh = int(time.strftime("%H"))
        curr_mm = int(time.strftime("%M"))
        if curr_hh == hh and curr_mm == mm:
            music = pyglet.media.load("1.mp3")
            music.play()
            pyglet.app.run()
            pyglet.exit()
            check = False
            exit()
        else:
            time.sleep(30)

if __name__ == "__main__":
    print """
    1. Play alarm after X minutes.
    2. Play alarm at specified time
    """
    print
    choice = int(raw_input("Enter your choice: "))

    if choice == 1:
        print "Current time in HH:MM format is: %s" % time.strftime("%H:%M")
        mins = int(raw_input("How many minutes from now do you want to play the alarm?: "))
        hh = mins / 60
        hours = hh + int(time.strftime("%H"))
        mins = mins % 60
        mins = mins + int(time.strftime("%M"))
        alarm(hours, mins)
    elif choice == 2:
        print "Current time in HH:MM format is: %s" % time.strftime("%H:%M")
        try:
            hhmm = raw_input("Enter time in HH:MM format: ")
            alarm_time = hhmm.split(':')
            if len(alarm_time) != 2:
                raise Exception

            alarm_time = [int(alarm_time[0]), int(alarm_time[1])]
            if not (alarm_time[0] in range(0, 24) and alarm_time[1] in range(0, 60)):
                raise Exception
        except:
            print "Invalid input"
        else:
            alarm(alarm_time[0], alarm_time[1])

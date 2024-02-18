#!/usrs/bin/python3
"""This code was adopted from Python Coding YouTube channel day 63..."""

import time
def countdown(time_sec):
    while time_sec:
        mins, secs = divmod(time_sec, 60)
        timeformat = '{:02d}:{:02d}'.format(mins, secs)
        print(timeformat, end='\r')
        time.sleep(1)
        time_sec -= 1

    print("stop")
num = int(input("Set your time : "))
countdown(num)


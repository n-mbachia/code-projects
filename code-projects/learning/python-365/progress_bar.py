#!/usr/bin/python3

'''This code was adopted from Python Coding YouTube channel day 49... '''

import sys, time

def progress_bar(count, total, suffix=''):
    """ Function takes three arguments"""
    bar_length = 60
    filled_length = int(round(bar_length * count/ float(total)))

    percent = round(100.0 * count / float(total), 1)
    bar = '=' * filled_length + '-' * (bar_length - filled_length)
    
    sys.stdout.write('[%s] %s%s ...%s\r' % (bar, percent, '%', suffix))
    sys.stdout.flush()

for i in range(10):
    time.sleep(1)
    progress_bar(i, 10)


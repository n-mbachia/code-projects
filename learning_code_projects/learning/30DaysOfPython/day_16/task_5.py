#!/usr/bin/python3

"""Calculate the time difference between 1 January 1970 and now."""

import datetime

# Get the current date & time
now = datetime.datetime.now()

# Get the date and time from 1 January, 1970

time_then = datetime.datetime(1970, 1, 1)

# Calculate the time difference
time_diff = now - time_then

print(time_diff)

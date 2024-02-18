#!/usr/bin/python3

"""Today is 5 December, 2019. Change this time string to time."""

import datetime

# Create a datetime object from the given string
date_time_str = "5 December, 2019"
date_time_obj = datetime.datetime.strptime(date_time_str, "%d %B, %Y")

# Get the time from the datetime object
time = date_time_obj.time()

#Print the time
print(time)



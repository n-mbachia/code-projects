#!/usrs/bin/python3


"""Calculate the time difference between now and new year."""

import datetime

# Get the current date and time
now = datetime.datetime.now()

# Get the new year date and time
new_year = datetime.datetime(now.year + 1, 1, 1)

# Calculate the time difference
time_diff = new_year - now

# Print the time difference
print(time_diff)

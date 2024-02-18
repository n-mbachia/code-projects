#1/usr/bin/python3
"""Change the following into a lkst of concatenated string."""

names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]

full_names = [f'{first_name} {last_name}' for sublist in names for first_name, last_name in sublist]

print(full_names)


"""This code works by first iterating over the list of names and the sublist within each name. For each name, the code then creates a new string containing the first name and the last name, separated by a space.

Finally, the new string is added to the full_names list."""

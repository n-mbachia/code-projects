#!/usr/bin/python3

"""names = ['Finland', 'Sweden', 'Norway','Denmark','Iceland', 'Estonia','Russia']. Unpack the first five countries and store them in a variable nordic_countries, store Estonia and Russia in es, and ru respectively."""
names = ['Finland', 'Sweden', 'Norway', 'Denmark', 'Iceland', 'Estonia', 'Russia']

*names_list, es, ru = names

nordic_countries = names[:5]

print("Nordic countries:", nordic_countries)
print(es)
print(ru)

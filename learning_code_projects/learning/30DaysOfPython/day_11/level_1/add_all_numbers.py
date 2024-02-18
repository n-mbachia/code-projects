#!/usr/bin/python3
"""Write a function called add_all_nums which takes arbitrary number of arguments and sums all the arguments. Check if all the list items are number types. If not do give a reasonable feedback."""

def add_all_nums(*args):
   """Sum of all arguments, 
   
   Arguments:
     *args = abitrary number of argumners
   
   Returns:
     returns the sum of arguments, if they are all numbers 
     otherwise raises a TypeError exception
   """

   total = 0
   for i in args:
      try:
         total += int(i)
      except ValueError: 
         return None
   return(total)
print(add_all_nums(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))

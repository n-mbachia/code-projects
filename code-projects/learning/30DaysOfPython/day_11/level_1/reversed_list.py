#!/usr/bin/python3
def reverse_list(list1):
  """Reverses the order of a list.

  Args:
    list1: A list.

  Returns:
    A reversed list.
  """

  reversed_list = []
  for i in range(len(list1) - 1, -1, -1):
    reversed_list.append(list1[i])
  return reversed_list
print(reverse_list([1, 2, 3, 4, 5]))
print()
print(reverse_list(['A', 'B', 'C']))


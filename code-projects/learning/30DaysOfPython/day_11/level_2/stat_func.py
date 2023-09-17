#!/usr/bin/python3
"""Write different functions which take lists. They should calculate_mean, calculate_median, calculate_mode, calculate_range, calculate_variance, calculate_std (standard deviation)."""

import statistics

def calculate_mean(list_of_numbers):
  """Calculates the mean of a list of numbers.

  Args:
    list_of_numbers: A list of numbers.

  Returns:
    The mean of the list of numbers.
  """

  return statistics.mean(list_of_numbers)

def calculate_median(list_of_numbers):
  """Calculates the median of a list of numbers.

  Args:
    list_of_numbers: A list of numbers.

  Returns:
    The median of the list of numbers.
  """

  return statistics.median(list_of_numbers)

def calculate_mode(list_of_numbers):
  """Calculates the mode of a list of numbers.

  Args:
    list_of_numbers: A list of numbers.

  Returns:
    The mode of the list of numbers.
  """

  return statistics.mode(list_of_numbers)

def calculate_range(list_of_numbers):
  """Calculates the range of a list of numbers.

  Args:
    list_of_numbers: A list of numbers.

  Returns:
    The range of the list of numbers.
  """

  return max(list_of_numbers) - min(list_of_numbers)

def calculate_variance(list_of_numbers):
  """Calculates the variance of a list of numbers.

  Args:
    list_of_numbers: A list of numbers.

  Returns:
    The variance of the list of numbers.
  """

  return statistics.variance(list_of_numbers)

def calculate_std(list_of_numbers):
  """Calculates the standard deviation of a list of numbers.

  Args:
    list_of_numbers: A list of numbers.

  Returns:
    The standard deviation of the list of numbers.
  """

  return statistics.stdev(list_of_numbers)

def print_statistics(list_of_numbers):
  """Prints the statistics of a list of numbers.

  Args:
    list_of_numbers: A list of numbers.
  """

  print(f"Mean: {calculate_mean(list_of_numbers)}")
  print(f"Median: {calculate_median(list_of_numbers)}")
  print(f"Mode: {calculate_mode(list_of_numbers)}")
  print(f"Range: {calculate_range(list_of_numbers)}")
  print(f"Variance: {calculate_variance(list_of_numbers)}")
  print(f"Standard deviation: {calculate_std(list_of_numbers)}")

def main():
  """Prompts the user for a range of numbers and prints the statistics of the list."""

  # Prompt the user for a range of numbers.
  start = int(input("Enter the start of the range: "))
  end = int(input("Enter the end of the range: "))

  # Create a list of numbers from the start to the end of the range.
  list_of_numbers = []
  for i in range(start, end + 1):
    list_of_numbers.append(i)

  # Print the statistics of the list of numbers.
  print_statistics(list_of_numbers)

if __name__ == "__main__":
  main()

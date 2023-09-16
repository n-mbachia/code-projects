#!/usrs/bin/python3
"""Write a function called calculate_slope which return the slope of a linear equation"""

def calculate_slope(x1, y1, x2, y2):
  """Calculates the slope of a linear equation.

  Args:
    x1: The x-coordinate of the first point.
    y1: The y-coordinate of the first point.
    x2: The x-coordinate of the second point.
    y2: The y-coordinate of the second point.

  Returns:
    The slope of the linear equation.
  """

  slope = (y2 - y1) / (x2 - x1)
  return slope

print(calculate_slope(2, 3, -4, 5))

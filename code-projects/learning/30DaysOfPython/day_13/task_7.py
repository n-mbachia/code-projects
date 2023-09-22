#!/usr/bin/python3
"""Write a lambda function which can solve a slope or y-intercept of linear functions."""

def slope_or_y_intercept(x1, y1, x2, y2, type):
  """Calculates the slope or y-intercept of a linear function using list comprehensions.

  Args:
    x1: The x-coordinate of the first point.
    y1: The y-coordinate of the first point.
    x2: The x-coordinate of the second point.
    y2: The y-coordinate of the second point.
    type: The type of calculation to perform, either "slope" or "y-intercept".

  Returns:
    The slope or y-intercept of the linear function.
  """

  if type == "slope":
    return [(y2 - y1) / (x2 - x1)]
  elif type == "y-intercept":
    return [y1 - slope_or_y_intercept(x1, y1, x2, y2, "slope")[0] * x1]
  else:
    raise ValueError("Invalid type: {}".format(type))

# Example usage:

# Calculate the slope of the line passing through the points (1, 2) and (3, 4)
slope = slope_or_y_intercept(1, 2, 3, 4, "slope")
print(slope)

# Calculate the y-intercept of the line passing through the points (1, 2) and (3, 4)
y_intercept = slope_or_y_intercept(1, 2, 3, 4, "y-intercept")
print(y_intercept)

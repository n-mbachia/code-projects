#!/usrs/bin/python3
"""Quadratic equation is calculated as follows: ax² + bx + c = 0. Write a function which calculates solution set of a quadratic equation, solve_quadratic_eqn."""

def solve_quadratic_eqn(a, b, c):
  """Calculates the solution set of a quadratic equation.

  Args:
    a: The coefficient of the x^2 term.
    b: The coefficient of the x term.
    c: The constant term.

  Returns:
    A tuple containing the two solutions to the quadratic equation, or None if
    there are no real solutions.
  """

  discriminant = b**2 - 4 * a * c
  if discriminant < 0:
    return None
  elif discriminant == 0:
    return (-b / (2 * a),)
  else:
    return ((-b + discriminant**0.5) / (2 * a),
            (-b - discriminant**0.5) / (2 * a))

print(solve_quadratic_eqn(1, 2, 1))


"""The output (-1.0,) from the solve_quadratic_eqn(1, 2, 1) function indicates that the quadratic equation has one real solution, which is -1.0.

This can be explained by the quadratic formula, which is as follows:

x = (-b ± √(b² - 4ac)) / 2a
where a, b, and c are the coefficients of the quadratic equation.

In the case of the quadratic equation 1x² + 2x + 1 = 0, the coefficients are a = 1, b = 2, and c = 1. Substituting these values into the quadratic formula, we get the following:

x = (-2 ± √(2² - 4 * 1 * 1)) / 2 * 1
x = (-2 ± √0) / 2
x = (-2 ± 0) / 2
x = -1
Therefore, the quadratic equation 1x² + 2x + 1 = 0 has one real solution, which is -1.0.

The solve_quadratic_eqn(1, 2, 1) function returns a tuple containing the two solutions to the quadratic equation. If the quadratic equation has one real solution, the function returns a tuple containing the solution only once. This is why the output is (-1.0,) instead of (-1.0)."""

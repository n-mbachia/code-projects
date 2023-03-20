#!/user/bin/python3
""" explore the lambda function"""

def compose1(f, g):
    """Function that takes two functions as its arguments"""
    return lambda x: f(g(x)) 
    # Function that applies functions f and g to an input argument x in sequence.
    """The lambda function is used to create an anonymous function that takes a single argument in this case x. Specifically, the returned function takes an input argument x, applies g(x) first, and then applies f to the result of g(x). The result of the composed function is the output of f(g(x))."""
f = compose1(lambda x: x * x, # Lambda function that squares input
             lambda y: y + 1) # Lambda function that add 1 to input
result = f(12)
"""Then, the code calls the lambda function f with an argument of 12, which first applies g to 12 (adding 1), then applies f to the result (squaring the result of g(12)), and returns the final result"""

print(result) # code prints the result of the lambda function call, which is 169.

# This file is showing how a function can be used as an argument 

def summation(n, term):
    """ Function takes care of actual summation process.
    
    where n is user input while term is the function passed as an argument.
    """
    total, k = 0, 1
    while k <= n:
        total, k = total + term(k), k + 1 # tuple unpacking to assign to two variables at once
        """ current value 'k' incremented by 1 using 'k + 1'
        'term' function called with new value of 'k'. The current value 'total' is added to value from step 2 using 'total + term(k)'. 
        Result of step 3 is a tuple with two values: updated value of 'total' and updated value of 'k+1'. Tuple from step 4 is unpacked using tuple unpacking. First value is updated value of 'total' assigned to 'total'.
        The second value is updated value of 'k+1' is assignmed to variable 'k'. The while loop continues until the condition 'k <= n' is no longer true, at which point final value of 'total' is retuned. 
        """
    return total

def cube(x):
    return x*x*x

def sum_cubes(n):
    return summation(n, cube) # function cube passed as argument

def identity(x):
    return x

def sum_naturals(n):
    """ A nutural number is a positive number that is >= 1. They are used for counting, measure quantities, represent size of sets and define the order of elements in a sequence or series. They are used in all mathematical branches.
    """
    return summation(n, identity) # function identity passed as argument
n = int(input("Enter a number: "))

def pi_term(x):
    """ 'pi_term" function is a mathematical function that calculates specific term of the Leibiz formula for pi which is an infinate series used to approximate the value of pi, as shown in the shortest formula as shown below
    """
    return 8 / ((4*x-3) * (4*x-1)) # Leibiz formula

def pi_sum(n):
    return summation(n, pi_term) # Function pi_term passed as argument

# try-except statement used to handle input error and provide clear error message.
try:
    n = int(n) # user input defined and accepted as integer
    result_cubes = sum_cubes(n) # calls sum_cubes function
    result_naturals = sum_naturals(n) # calls sum_naturals function 
    result_pi = pi_sum(n) # calls pi_sum function
    print(f"The sum of the cubes from 1 to {n} is: {result_cubes}")
    print(f"The sum of the natural numbers from 1 to {n} is: {result_naturals}")
    print(f"The sum of pi from 1 to {n} is: {result_pi}")
except ValueError: # Outputs error message
    print("Error: Input must be an integer")


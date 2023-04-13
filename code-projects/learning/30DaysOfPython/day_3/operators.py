age = 32
print(age)
height= 5.4
print(height) 
"""complex_number = j + 3
print(complex_number)"""
height = int(input("Enter the height of a triangle: "))
base = int(input("Enter the base of a triangle: "))
area_of_triangle = (0.5 * base * height)
print('The area of a triangle is ', area_of_triangle)
print()
side_a = int(input("Enter the side a of a triangle: "))
side_b = int(input("Enter the side b of a triangle: "))
side_c = int(input("Enter the side c of a traingle: "))
perimeter_of_triangle = (side_a + side_b + side_c)
print("The periemter of the triangle is ", perimeter_of_triangle)
print()
length = int(input("Enter length of a rectangle: "))
width = int(input("Enter width of a rectangle: "))
area_of_rectangle = length * width
perimeter_of_rectangle = 2 * (length + width)
print('The area of a rectangle is ', area_of_rectangle, 
      'periemter of the same rectangle is ', perimeter_of_rectangle)
print()
radius = int(input("Enter the radius of a circle: "))
pi = 3.142
area_of_circle = (pi * radius ** 2)
circu_of_circle = (2 * pi * radius)
print('The area of the cicle is ', area_of_circle, 
      'and circumference is ', circu_of_circle)
print()
x = (1, 0)
y = (0, -2)
slope_m = ((y[0] - x[0]) ** 2 + (y[1] - x[1]) ** 2) ** 0.5
print("The slope of x-intercepot and y-intercept of y = 2x -2 is ",slope_m)
print()
x = (2, 2)
y = (6, 10)
slope = ((y[1] - x[0]) ** 2 + (y[1] - x[0]) ** 2) **0.5
print("Euclidean diustance between point(2, 2) anbd point (6, 10) is ", slope)
print()
print(slope_m <= slope)
print()
# Calculate the value of y for x = 2
x = 2
y = x**2 + 6*x + 9
print("When x =", x, ", y =", y)

# Find the x value at which y is equal to 0
a = 1
b = 6
c = 9
discriminant = b**2 - 4*a*c
x1 = (-b + discriminant**0.5) / (2*a)
x2 = (-b - discriminant**0.5) / (2*a)
print("The x values at which y is 0 are", x1, "and", x2)
print()
print(len('python') and len('dragon'))
print()
print('on' in 'python' and 'on' in 'dragon')
print()
print('jargon' in 'I hope this course is not full of jargon')
# print('on' not 'python' and 'on' not 'dragon')
print()
print(float(len('python')))
print()
print(2 % 2 == 0)
print()
print(7/3 == 2.7)
print(type('10') == type(10))
print()
print(int(9.8) == 10)
print()
hours = int(input("Enter hours worked: "))
hourly_rate =int(input("Enter rate per hour: "))
weekly_earnings = hours * hourly_rate
print("Your weekly earning is: ", weekly_earnings)
sec_in_min = 60
sec_in_hour = sec_in_min * 60
sec_in_day = sec_in_hour * 24
sec_in_year = sec_in_day * 365
age = int(input("Enter your current age: "))
sec_lived = sec_in_year * age
print("You have lived for ", sec_lived, "seconds")
print()
# Display the table
print("1 1 1 1 1")
print("2 1 2 4 8")
print("3 1 3 9 27")
print("4 1 4 16 64")
print("5 1 5 25 125")
print()

#!/usrs/bin/python3

"""This is a grading score application
80 - 100, A
70 -79, B
60 - 69, C
50 - 59, D
0 - 49, F
"""

score = int(input("Enter the score for grading:"))
if score >= 80:
    print("A")
elif score >= 70:
    print("B")
elif score >= 60:
    print("C")
elif score >= 50:
    print("D")
else:
    print("F")

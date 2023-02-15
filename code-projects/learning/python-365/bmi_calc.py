#1/usr/bin/python3

import tkinter as tk

def calculate_bmi():
    height = float(entry_height.get())
    weight = float(entry_weight.get())
    height = height / 100
    bmi = weight / (height * height)
    bmi = round(bmi)
    label_result.config(text=f"Your Body Mass Index is: {bmi}")
    
    if bmi > 0:
        if bmi <= 16:
            label_status.config(text="You are severely underweight. You seek nutritional advice!")
        elif bmi <= 18.5:
            label_status.config(text="You are underweight. Need to eat some beef and fiber.")
        elif bmi <= 25:
            label_status.config(text="You are Healthy, Very impressive!")
        elif bmi <= 30:
            label_status.config(text="You are overweight. Lose a few kilograms!")
        else:
            label_status.config(text="You are obese, It surely sucks to be you! Discipline, commitment and serious lifestyle change required!")
    else:
        label_status.config(text="Please enter valid details")

root = tk.Tk()
root.title("BMI Calculator")

frame_input = tk.Frame(root)
frame_input.pack()

label_height = tk.Label(frame_input, text="Enter your height in centimeters:")
label_height.pack(side="left")

entry_height = tk.Entry(frame_input)
entry_height.pack(side="left")

frame_input = tk.Frame(root)
frame_input.pack()

label_weight = tk.Label(frame_input, text="Enter your weight in kilograms:")
label_weight.pack(side="left")

entry_weight = tk.Entry(frame_input)
entry_weight.pack(side="left")

frame_result = tk.Frame(root)
frame_result.pack()

label_result = tk.Label(frame_result)
label_result.pack(side="left")

frame_status = tk.Frame(root)
frame_status.pack()

label_status = tk.Label(frame_status)
label_status.pack(side="left")

button_calculate = tk.Button(root, text="Calculate", command=calculate_bmi)
button_calculate.pack()

root.mainloop()

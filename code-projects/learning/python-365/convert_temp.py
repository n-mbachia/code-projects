#!/usr/bin/python3

import tkinter as tk

def convert_to_celsius():
    temperature = float(entry_temperature.get())
    c = (temperature-32) * 5/9
    result_label.config(text=f"{c:.2f}°C")

def convert_to_fahrenheit():
    temperature = float(entry_temperature.get())
    f = (temperature * 9/5) + 32
    result_label.config(text=f"{f:.2f}°F")

root = tk.Tk()
root.title("Temperature converter")

label_temperature = tk.Label(root, text="Temperature: ")
label_temperature.grid(row=0, column=0, sticky='W')

entry_temperature = tk.Entry(root)
entry_temperature.grid(row=0, column=1)

convert_to_celsius_button = tk.Button(root, text="Convert to Celsius", command=convert_to_celsius)
convert_to_celsius_button.grid(row=1, column=0)

convert_to_fahrenheit_button = tk.Button(root, text="Convert to Fahrenheit", command=convert_to_fahrenheit)
convert_to_fahrenheit_button.grid(row=1, column=1)

result_label = tk.Label(root, text="")
result_label.grid(row=2, column=0, columnspan=2, pady=10)

root.mainloop()

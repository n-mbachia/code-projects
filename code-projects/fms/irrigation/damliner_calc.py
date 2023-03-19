#!/usr/bin/python3

import tkinter as tk

def calculate_liner():
    """Function calculates dam linere required for a rectangular shaped pond"""
    # Get the dimensions of the pond from the user
    pond_length = float(length_entry.get())
    pond_width = float(width_entry.get())
    pond_depth = float(depth_entry.get())

    # Calculate the required size of the dam liner
    damliner_length = pond_length + (2 * pond_depth) + 2
    damliner_width = pond_width + (2 * pond_depth) + 2

    # Calculate the total square meters required for the dam liner
    total_area = damliner_length * damliner_width

    # Calculate the total cost of the required dam liner
    price = float(price_entry.get())
    total_cost = price * total_area

    # Calculate the total cubic meters the dam can hold when at full capacity
    total_volume = pond_length * pond_width * pond_depth

    # Update the labels with the results
    liner_size_label.config(text="The required size of the dam liner is {} meters by {} meters.".format(damliner_length, damliner_width))
    area_label.config(text="The total square meters required for the dam liner is {:,.2f} square meters.".format(total_area))
    cost_label.config(text="The total cost of the required dam liner is {:,.2f}.".format(total_cost))
    volume_label.config(text="The total cubic meters the dam can hold when at full capacity is {:,.2f} cubic meters.".format(total_volume))

# Create the main window
window = tk.Tk()
window.title("Dam Liner Calculator")

# Create the input fields and labels
length_label = tk.Label(window, text="Length (meters):")
length_label.grid(row=0, column=0)
length_entry = tk.Entry(window)
length_entry.grid(row=0, column=1)

width_label = tk.Label(window, text="Width (meters):")
width_label.grid(row=1, column=0)
width_entry = tk.Entry(window)
width_entry.grid(row=1, column=1)

depth_label = tk.Label(window, text="Depth (meters):")
depth_label.grid(row=2, column=0)
depth_entry = tk.Entry(window)
depth_entry.grid(row=2, column=1)

price_label = tk.Label(window, text="Price per square meter:")
price_label.grid(row=3, column=0)
price_entry = tk.Entry(window)
price_entry.grid(row=3, column=1)

# Create the button to calculate the dam liner size
calculate_button = tk.Button(window, text="Calculate", command=calculate_liner)
calculate_button.grid(row=4, column=0, columnspan=2)

# Create the labels to display the results
liner_size_label = tk.Label(window, text="")
liner_size_label.grid(row=5, column=0, columnspan=2)

area_label = tk.Label(window, text="")
area_label.grid(row=6, column=0, columnspan=2)

cost_label = tk.Label(window, text="")
cost_label.grid(row=7, column=0, columnspan=2)

volume_label = tk.Label(window, text="")
volume_label.grid(row=8, column=0, columnspan=2)

# Run the main loop
window.mainloop()

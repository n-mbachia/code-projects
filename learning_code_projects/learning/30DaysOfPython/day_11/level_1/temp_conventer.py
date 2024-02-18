#!/usr/bin/python3
"""Temperature in °C can be converted to °F using this formula: °F = (°C x 9/5) + 32. Write a function which converts °C to °F, convert_celsius_to-fahrenheit."""

def convert_celsius_to_fahrenheit(c):
    """Converts temperature from Temperature in °C to °F,

    Arguments:
     Celcius 
    
     Returns:
      Fahremheit
    """
    fahrenheit = (c * 9/5) + 32
    return(fahrenheit)
print(convert_celsius_to_fahrenheit(32))

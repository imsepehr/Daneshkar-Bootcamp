# get a temprature in centigrations then convert it to farenheit format

centigrade_temperature = float(input())

Fahrenheit_temperature = (centigrade_temperature * 1.8) - 32 

print("{:.1f}".format(Fahrenheit_temperature)) # show Farerenheit temperature in float format with one decimal place
from temperature.celsius_to_fahrenheit import celsius_to_fahrenheit
from temperature.fahrenheit_to_celsius import fahrenheit_to_celsius
from temperature.celsius_to_kelvin import celsius_to_kelvin

print("Enter a number between 1-3 to get the corresponding conversion:")
print("1. Celsius to Fahrenheit")
print("2. Fahrenheit to Celsius")
print("3. Celsius to Kelvin")

opt = int(input("Enter Number: "))

if opt == 1:
    c = float(input("Enter temperature in Celsius: "))
    print("Fahrenheit:", celsius_to_fahrenheit(c))

elif opt == 2:
    f = float(input("Enter temperature in Fahrenheit: "))
    print("Celsius:", fahrenheit_to_celsius(f))

elif opt == 3:
    c = float(input("Enter temperature in Celsius: "))
    print("Kelvin:", celsius_to_kelvin(c))

else:
    print("Please enter a valid number.")
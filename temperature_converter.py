# Temperature Converter Program

# Take temperature input from user
temp = float(input("Enter the temperature value: "))
unit = input("Enter the unit (C for Celsius, F for Fahrenheit, K for Kelvin): ").upper()

if unit == "C":
    # Celsius to Fahrenheit and Kelvin
    fahrenheit = (temp * 9/5) + 32
    kelvin = temp + 273.15
    print("Temperature in Fahrenheit:", fahrenheit)
    print("Temperature in Kelvin:", kelvin)

elif unit == "F":
    # Fahrenheit to Celsius and Kelvin
    celsius = (temp - 32) * 5/9
    kelvin = celsius + 273.15
    print("Temperature in Celsius:", celsius)
    print("Temperature in Kelvin:", kelvin)

elif unit == "K":
    # Kelvin to Celsius and Fahrenheit
    celsius = temp - 273.15
    fahrenheit = (celsius * 9/5) + 32
    print("Temperature in Celsius:", celsius)
    print("Temperature in Fahrenheit:", fahrenheit)

else:
    print("Invalid unit! Please enter C, F, or K.")

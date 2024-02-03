while True:
    celcius = float(input("\nCelcius temperature: "))
    fahrenheit = celcius * 9/5 +32
    print("Your temperature in fahrenheit is: ", fahrenheit , str("°F" ))
    fahrenheit2 = float(input("\nFahrenheit temperature: "))
    celcius2 = 5/9 * (fahrenheit2-32)
    print("Your temperature in celcius is: " , celcius2, str("°C"))
def count_from_fahrenheit(fahrenheit):
    fahrenheit_to_celsius = (fahrenheit - 32) * 5/9
    fahrenheit_to_reamur = (fahrenheit - 32) * 4/9
    fahrenheit_to_kelvin = (fahrenheit - 32) * 5/9 + 273.15
    print("Celcius : ", fahrenheit_to_celsius)
    print("Reamur : ", fahrenheit_to_reamur)
    print("Kelvin : ", fahrenheit_to_kelvin)
    print("\n")
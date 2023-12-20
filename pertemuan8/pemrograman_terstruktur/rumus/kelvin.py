def count_from_kelvin(kelvin):
    kelvin_to_celsius = kelvin - 273.15
    kelvin_to_fahrenheit = (kelvin - 273.15) * 9/5 + 32
    kelvin_to_reamur = (kelvin - 273.15) * 4/5
    print("Celcius : ", kelvin_to_celsius)
    print("Fahrenheit : ", kelvin_to_fahrenheit)
    print("Reamur : ", kelvin_to_reamur)
    print("\n")
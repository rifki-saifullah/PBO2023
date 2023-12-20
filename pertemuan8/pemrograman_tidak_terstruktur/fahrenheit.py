print("Hitung Suhu Fahrenheit ke Suhu lainnya")

fahrenheit = float(input("Masukkan suhu dalam Fahrenheit : "))

celcius = (fahrenheit - 32) * 5/9
reamur = (fahrenheit - 32) * 4/9
kelvin = (fahrenheit - 32) * 5/9 + 273.15
print("Celcius : ", celcius)
print("Reamaur : ", reamur)
print("Kelvin : ", kelvin)

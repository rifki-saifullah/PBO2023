print("Hitung Suhu Kelvin ke Suhu lainnya")

kelvin = float(input("Masukkan suhu dalam Kelvin : "))

celsius = kelvin - 273.15
fahrenheit = (kelvin - 273.15) * 9/5 + 32
reamur = (kelvin - 273.15) * 4/5

print("Celcius : ", celsius)
print("Fahrenheit : ", fahrenheit)
print("Reamur : ", reamur)
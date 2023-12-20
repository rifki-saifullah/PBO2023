from rumus.celsius import count_from_celsius
from rumus.fahrenheit import count_from_fahrenheit
from rumus.reamur import count_from_reamur
from rumus.kelvin import count_from_kelvin

while(True):
    print("Kalkulator Suhu")
    print("Menu")
    print("1. Celsius to All")
    print("2. Fahrenheit to All")
    print("3. Reamur to All")
    print("4. kelvin to All")
    print("0. Keluar")
    
    pilihan = int(input("Masukkan pilihan : "))
    print("\n")
    if pilihan == 1:
        celsius = int(input("Masukkan suhu dalam celsius : "))
        count_from_celsius(celsius)
    elif pilihan == 2:
        fahrenheit = int(input("Masukkan suhu dalam fahrenheit : "))
        count_from_fahrenheit(fahrenheit)
    elif pilihan == 3:
        reamur = int(input("Masukkan suhu dalam reamur : "))
        count_from_reamur(reamur)
    elif pilihan == 4:
        kelvin = int(input("Masukkan suhu dalam kelvin : "))
        count_from_kelvin(kelvin)
    elif pilihan == 0:
        break
    else :
        print("Pilihan tidak diketahui")
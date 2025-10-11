def celsius_ke_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def celsius_ke_reamur(celsius):
    return (4/5) * celsius          

while True:
    print("program konversi suhu")
    print("1. suhu celsius")
    print("2. suhu reamur")
    print("3. suhu fahrenheit")
    print("4. Keluar")
    pilihan = input("msukan pilihan anda ")

    if pilihan == "1":
        celsius = int(input("masukan suhu celsius "))
        print(f"suhu celsius = {celsius}")
    elif pilihan == "2":
        celsius = float(input("suhu celsius "))
        reamur = celsius_ke_reamur(celsius)
        print(f"suhu reamur = {reamur}")
    elif pilihan == "3":
        celsius = float(input("masukan suhu celsius "))
        fahrenheit = celsius_ke_fahrenheit(celsius)
        print(f"suhu fahrenheit = {fahrenheit}")
    elif pilihan == "4":
        print("Keluar dari program")
        break
    else:
        print("Pilihan anda salah")
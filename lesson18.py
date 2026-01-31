def kalkulator():
    try:
        angka1 = float(input("masukan angka pertama: "))
        angka2 = float(input("masukan angka kedua: "))
        operasi = input("masukan operasi (+,-,*,/):")
        if operasi =="+":
            hasil = angka1 + angka2
        elif operasi =="-":
            hasil = angka1 - angka2
        elif operasi =="*":
            hasil = angka1 * angka2
        elif operasi =="/":
            hasil = angka1 / angka2
        else:
            print("opersi tidak valid")
            return print(f"hasil:{hasil}")
    except ValueError:
        print("input harus angka")
    except ZeroDivisionError:print("Tidak bisa dibagi dengan nol!")
    
while True:
    print("/nkalkulator Sederhana")
    kalkulator
    lagi = input("apakah anda ingin menghitung lagi? (ya/tidak):")
    if lagi.lower()!="ya":
        print("Terima kasih! sampai jumpa.")
        break

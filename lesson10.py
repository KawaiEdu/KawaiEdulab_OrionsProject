# fungsi lambda untuk operasi matematika
tambah = lambda x, y: x + y
kurang = lambda x, y: x - y
kali = lambda x, y: x * y
bagi = lambda x, y: x / y

while True:
    # memintak input dari pengguna
    print("/nselamat datang di kalkulator lambda!") # ini inputan angka pertama
    x = float(input("masukan angka pertama kamu: ")) # Ini Inputan angka kedua
    y = float(input("masukan angka ke dua: "))

    if x != 0 and y != 0:
        operasi = input("pilih operasi(+,-,*,/): ")
        # menjalankan fungsi berdasarkan operasi yang di pilih
        if operasi =='+':
            print("hasil:", tambah(x,y))
        elif operasi =='-':
            print("hasil:", kurang(x,y)) 
        elif operasi =='*':
            print("hasil:", kali(x,y))
        elif operasi =='/':
            print("hasil:", bagi(x,y))
        else:
            print("operasi tidak valid!")
    else:
        print("eror tidak bisa di bagi dengan nol")
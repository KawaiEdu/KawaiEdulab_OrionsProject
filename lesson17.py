def tulis_catatan():
    catatan = input("masukan catatan anda:")
    with open("ORIONS.txt","a") as file:
        file.write(catatan + "\n")
        print("catatan berhasil disimpan!")

def baca_catatan():
    try:
        with open("ORIONS.txt","r") as file:
            print("\ncatatan harian anda:")
            print(file.read())
    except FileNotFoundError:
        print("belum ada catatan yang tersimpan.")
        
while True:
    print("\npilih menu:")
    print("1. tulis catatan")
    print("2. baca catatan")
    print("3. keluar")
    pilihan = input("masukkan pilihan (1/2/3):")
    
    if pilihan == "1":
        tulis_catatan()
    elif pilihan == "2":
        baca_catatan()
    elif pilihan == "3":
        print("terima kasih! sampai jumpa.")
        break
    else:
        print("pilihan tidak valid. silakan coba lagi.")
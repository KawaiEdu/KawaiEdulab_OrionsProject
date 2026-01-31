#Fungsi untuk menampilkan menu
def tampilkan_menu():
    print("/nSelamat datang di program daftar tugas!")
    print("1. Tambah tugas")
    print("2. tampilan daftar tugas")
    print("3. hapus tugas")
    print("4. simpan daftar ke file")
    print("5. muat daftar ke file")
    print("6. keluar")
    
#fungsi untuk menambah tugas
def tambah_tugas(daftar):
    tugas = input("masukan nama tugas: ")
    daftar.append(tugas)
    print("{}berhasil ditambah ke daftar tugas.".format(tugas))
    
# Fungsi untuk menampilkan daftar tugas
def tampikan_daftar(daftar):
    if daftar:
        print("\ndaftar tugas:")
        for i, tugas in enumerate(daftar, start=1):
            print("{}.{}".format(i,tugas))
    else:
        print("daftar tugas kosong.")
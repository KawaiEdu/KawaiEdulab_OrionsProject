daftar_belanja = []

while True:
    print("\ndaftar belanja:", daftar_belanja)
    print("1. tambah item")
    print("2. hapus item")
    print("3. keluar")
    pilihan = input("pilih opsi (1/2/3): ")

    if pilihan =="1":
        item = input("masukan item yang ingin ditambah:")
        daftar_belanja.append(item)
    elif pilihan =="2":
        item = input("masukkan item yang ingin dihapus:")
        if item in daftar_belanja:
            daftar_belanja.remove(item)
        else:
            print("item tidak ditemukan dalam daftar!")
    elif pilihan =="3":
        print("terima kasi telah menggunakkan program ini!")
        break
    else:
        print("pilihan tidak valid, coba lagi.")+
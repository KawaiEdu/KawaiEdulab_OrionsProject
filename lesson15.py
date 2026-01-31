daftar_belanja = set()

while True:
    item = input("masukan item belanja(atau'selesai' untuk brhenti):")
    if item.lower() == "selesai":
        break
    daftar_belanja.add(item)
    
    print("daftar belanja unik anda:")
    for item in daftar_belanja:
        print(f"-{item}")
    
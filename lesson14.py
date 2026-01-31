kamus_buah = {
  "apel":"buah berwarna merah",
  "jeruk":"buh berwarna orenye",
  "pisang":"buah berwa kuning"
}

buah = input("masukan nama buah: ")
if buah in kamus_buah:
    print(f"{buah}:{kamus_buah[buah]}")
else:
    print("buah tidak ditemuakan dalam kamus.")
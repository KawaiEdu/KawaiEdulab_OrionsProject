buah_favorit_1 ={"apel","jeruk","pisang"}
buah_favorit_2 ={"jeruk","mangga","pisang"}

# buah yang sama
sama = buah_favorit_1 .intersection(buah_favorit_2)
print("buah yang sama disukai:",sama)

# buah yang brbeda
beda1 = buah_favorit_1 .difference(buah_favorit_2)
beda2 = buah_favorit_2 .difference(buah_favorit_1)
print("buah yang hanya disukai orang pertama:",beda1)
print("buah yang hanya disukai orang krdua:",beda2)
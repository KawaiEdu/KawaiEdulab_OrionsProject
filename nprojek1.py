suhu = int(input("masukan suhu"))
if suhu <10:
    print("cuaca: dingin \n pakai jaket tebal")
elif 10 <= suhu <=25:
    print("cuaca sejuk \n minum minuman hangat")
elif 26 <= suhu <=35:
    print("cuaca: hangat \n piknik")
else:
    print("cuaca: panas")
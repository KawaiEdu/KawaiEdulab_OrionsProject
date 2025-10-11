suhu=int(input("masukan suhu : "))
if suhu >30:
    print("sangat panas")
elif 30>= suhu >27:
    print("panas")
elif 27 >= suhu >22:
    print("hangat")
elif 22 >= suhu > 16:
     print("dingin")
else:
    print("dingin sekali")
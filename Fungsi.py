def salam():
    print("Hello, Selamat Pagi")

salam()

def luas_segitiga(alas , tinggi):
    luas = (alas * tinggi) / 2
    print("Luas segitiga: , %f" % luas)

luas_segitiga(4,6)

def luas_segitiga2(alas , tinggi):
    luas = (alas * tinggi) / 2
    return luas
print("Luas Segitiga : %d" %luas_segitiga2(4,6))
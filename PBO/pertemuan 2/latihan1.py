
class Mobil:
    #Membuat tipe variabel
    jumlah_tipemobil = 0
    #membuat construktor
    def __init__(self, warna, merk, harga):
        self.warnamobil = warna
        self.merkmobil = merk
        self.hargamobil = harga
        Mobil.jumlah_tipemobil += 1
    #Membuat method string
    def __str__(self):
        return f"{self.warnamobil}, {self.merkmobil}, {self.hargamobil}"
    #Membuat method baru custom
    def custom(self, custom):
        self.hargamobil += custom
    
#Membuat Objek Baru M1
M1 = Mobil("Putih", "Hyundai", 4900000000)
print(M1)
print("Jumlah Tipe Mobil Tersedia :", Mobil.jumlah_tipemobil)
M1.custom(6000000000)
print(M1)
#Membuat Objek Baru M2
M2 = Mobil("Hitam", "Toyota", 32000000000)
print(M2)
print("Jumlah Tipe Mobil Tersedia :", Mobil.jumlah_tipemobil)
#Membuat Objek Baru M3
M3 = Mobil("Merah", "Wuling", 29000000000)
print(M3)
print("Jumlah Tipe Mobil Tersedia :", Mobil.jumlah_tipemobil)
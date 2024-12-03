class Buku:
    jumlah_penerbitbuku = 0  
    
    def __init__(self, judul, penulis, tahun_terbit):
        self.judulbuku = judul
        self.penulisbuku = penulis
        self.tahunbuku = int(tahun_terbit)  
        Buku.jumlah_penerbitbuku += 1 

    def __str__(self):
        return f"{self.judulbuku}, {self.penulisbuku}, {self.tahunbuku}"

    def update(self, update):
        self.tahunbuku += update  



B1 = Buku("Dongeng Lengkap Kancil", "Kak Thifa", 2020)
print(B1)

B2 = Buku("Bukan Cinta Monyet", "Purnama Teduh", 2018)
print(B2)

print("Jumlah Buku Tersedia:", Buku.jumlah_penerbitbuku)

B2.update(5)
print(B2)
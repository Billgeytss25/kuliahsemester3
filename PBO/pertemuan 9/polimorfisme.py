# implementasi polimorfisme
class penjumlahan:
    def tambah(*num):
        return sum(num)
objek1 = penjumlahan
print(objek1.tambah(2,3,5,10))

#menggunakan default parameter
class default:
    def tambah2(self, a, b=0,c=0,d=0,e=0):
        print (f"Hasilnya {a+b+c+d+e}")
objek2 = default
objek2.tambah2(2,4,2)

#tanpa implementasi polmorfisme
class jumlah:
    def tambah1(n1, n2):
        print(f"hasilnya {n1+n2}")
objek3 = jumlah
objek3.tambah1(10,20)        
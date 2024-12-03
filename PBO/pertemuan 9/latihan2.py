#implementasi polimorfisme dngn mencari  bangun datars
class bangundatar:
    def luas(self):
        raise NotImplementedError("method ini wajib di implementasikan")
    
class segitiga(bangundatar): #abstrak class
    def __init__(self, sisi):
            self.sisi=sisi
    def luas2(self):
         print(f"luas segitiga adalah{self.sisi**2}")
class lingkaran(bangundatar): #kelasturunann 2
     def __init__(self, pi=3.14, r=0):
          self.pi = pi
          self.r = r
     def luas(self):
          print(f"luas lingkaran  adalah: {(self.pi*self.r)**2}")     

objek1 = persegi(2)
objek2 = segitiga(2,3)
objek1.luas()
objek2.luas()               
            
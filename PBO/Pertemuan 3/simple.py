# membuat sebuah super class
class animal:
    #membuat konstrktor untuk menampung attribut
    def __init__(self, name, ras):
        self.name = name
        self.ras = ras

    # membuat method bersuara
    def speakscat(self):
        print(f"{self.name} bisa berusara")
# membuat kelas turunan dari super kelas
class cat(animal):
    def sounds(self):
        print(f"Nama {self.name} dengan ras {self.ras} bersuara Meooowwww")
# membuat kelas 2 turunan dari super kelas
class dog(animal):
    def sounds(self):
        print(f"Nama{self.name} dengan ras {self.ras} berusara ANJINGGGGGG")        

# membuat objek 
cat = cat("kitty", "garong")
cat.speakscat()        
dog = dog("anjing" "minggir lu miskin")
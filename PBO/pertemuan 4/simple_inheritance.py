#Membuat sebuah super class
class Animal:
    #Membuat konstruktor menampung atribut
    def __init__(self, name, ras):
        self.name = name
        self.ras = ras

    #Membuat method  bersuara
    def Speaks(self):
        print(f"{self.name} bisa bersuara")

#Membuat kelas turunan dari super kelas
class Cat(Animal):
    def Sounds(self):
        print(f"Nama {self.name} dengan Ras {self.ras} bersuara MEWOOOOOOO")

class Dog(Animal):
    def Sounds(self):
        print(f"Nama {self.name} dengan Ras {self.ras} bersuara kGUKGUKKKK")

#Membuat objekk
Cat = Cat("Kitty," "Anggora")
cat.SpeaksCat()
Dog = Dog("Puppy," "Pitbull")
cat.SpeaksDog()

# membuat superclass animal
class animal:
   def __init__(self, name, age):
      self.name =name
      self.age = age
   
       
   
#membuat subclass dog yang mewarisi dari animal
class dog(animal):
   def __init__(self, name, age, ras):
    # inisiasi variabel name dan age dari super class
      super().__init__(name, age,)
      self.ras = ras
    # membuat method untuk kelas dog
   def speaksdog(self):
      print(f"dog {self.name} is sleeping")

dog1 = dog("buddy", 10, "labrador")
dog1.speaksdog()

# membuat kelas turunan dari kelas dog
class cat(dog):
   def __init__(self, name, age, ras, color):
      super().__init__(name, age, ras)
      self.color = color
   def speakscat(self):
      print(f"cat {self.name} from ras {self.ras} is mewwing")

dog1 = dog("buddy", 5, "labrador")
dog1.speaksdog()
cat1 = cat("mewing", 7, "black")
cat1.speakscat()

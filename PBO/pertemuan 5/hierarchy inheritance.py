# membuat konsep hierarchy inheritance
# membuat kelas parent /super class
class vechile:
    def __init__ (self, merk, model, year ):
       self.merk = merk
       self.model = model
       self.year = year
    def display_info(self):
       print(f"vechile: {self.year} {self.merk} {self.model}")

# membuat class turunan 1
class car(vechile):
   def __init__(self, merk, model, year, num_doors):
      super().__init__(merk, model, year)
      self.num_doors = num_doors
      # membuat method untuk kelas car
   def display_info(self):
      super().display_info()
      print(f"doors: {self.num_doors}")
# membuat kelas turunan 2
class motorcycle:
   def __init__(self, merk, model, year, cc):
      super().__init__(merk, model, year)
      self.cc = cc
      # membuat method untuk motor
   def display_info(self):
      super().display_info()
      print(f"cc:{self.cc}")

# objek turunan dari class car
car1 = car("toyota", "camry", 2023, 4)
car1.display_info()   
# membuat objek dari kelas turunan motor
motorcycle1 = motorcycle("honda", "yamaha", 2021, 2023)
motorcycle.display_info()      




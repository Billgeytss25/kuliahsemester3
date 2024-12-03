# membuat simple inheritance dg method pass
#membuat class animal
class animal:
    #membuat construktor
    def __init__(self, name, age):
     self.name = name
     self.age = age
# membuat method sound
    def sound(self):
       print(f"this {self.name} makes a sound") 

# membuat kelas turunan / subclass dog
class Dog(animal):
 pass

name = input("masukan nama anjing anda")
dog = Dog("Buddy", 3)
dog.sound()
    
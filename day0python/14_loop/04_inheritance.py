class Animal:#parent class(super class)
    location = "Australia"
    def _init_(self,name):
        self.name = name
    def speak(self):
        print("generic animal sound")

class Dog(Animal):
    def speak(self):
        print("woof!")
d = Dog("Bruno")
d.speak()
print(d.location)
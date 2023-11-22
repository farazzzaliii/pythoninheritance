
class Animal:
    def run(self, name):
        self.name = name
        print(f'{self.name} Is Runing')
 
 
 
class Dog(Animal):

class Cat(Animal):
 
 
 
dog = Dog()
dog.run("Dog")
cat = Cat()
cat.run("Cat")
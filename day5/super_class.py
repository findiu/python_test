#继承好处：
#1，继承父类有的方法
#2，方法的重写
#3，多态：
class Animal(object):
    def run(self):
        print('Animal is running....')
class Dog(Animal):
    def run(self):
        print('Dog is running....')
class Cat(Animal):
    def run(self):
        print('Cat is running....')
dog=Dog()
dog.run()
cat=Cat()
cat.run()
def run_twice(Animal):
    Animal.run()
run_twice(Animal())
run_twice(dog)
run_twice(cat)
class Tortoise(Animal):
    def run(self):
        print('Tortoise is running...')
run_twice(Tortoise())
class Timer(object):
    def run(self):
        print('Start...')
run_twice(Timer())
print(dir(dog))#获取一个对象的所有属性和方法
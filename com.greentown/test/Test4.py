# -*- coding:utf-8 -*-

# 定义父类 Animal
class Animal(object):

    def run(self):
        print 'Animal is running...'

# 定义子类 继承 Animal
class Dog(Animal):
    # 方法重写
    def run(self):
        print 'Dog is running...'
    # 子类添加新方法
    def eat(self):
        print 'Dog eat meat..'

# 定义子类 继承 Animal
class Cat(Animal):
    pass

dog = Dog()
cat = Cat()

# 继承使 子类 具有了 父类 的方法
dog.run()
cat.run()

print isinstance(dog, Dog) # True
print isinstance(dog, Animal) # True
#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 继承和多态
# 在OOP程序设计中，当我们定义一个class时，可以从某个现有的class继承，新的class成为子类(Subclass),而被继承的类成为基类
# (Base class, Super class)
# 例如
class Animal(object):

    def run(self):
        print 'Animal is running...'

# 当我们需要编写Dog和Cat类时，就可以直接从Animal类继承
class Dog(Animal):
    pass
class Cat(Animal):
    pass

# 对于Dog类来说，Animal就是他的父类，对于Animal来说，Dog就是他的子类，Cat和Dog类似
# 继承有什么好处？
# 最大的好处就是子类获得了父类的全部功能。
# 由于Animal实现了run方法，因此，Dog和Cat作为它的子类，什么事也没干，就自动拥有了run方法
dog = Dog()
dog.run()
cat = Cat()
cat.run()
# Animal is running...
# Animal is running...
# 当然，子类也可以增加一些方法
# 继承的第二个好处需要我们对代码做一点改进。理想的结果应该时调用dog.run()时，打印Dog is running... Cat类似
class Dog(Animal):
    def run(self):
        print 'Dog is running...'
    def eat(self):
        print 'Dog Eating meat...'

class Cat(Animal):
    def run(self):
        print 'Cat is running...'

dog = Dog()
dog.run()
dog.eat()
cat = Cat()
cat.run()
# Dog is running...
# Dog Eating meat...
# Cat is running...
# 当子类和父类都存在相同的run()方法时，就说，子类的run()覆盖了父类的run()
# 在代码运行时，总是会调用子类的run()，这样，就获得了继承的另一个好处：多态
# 要理解多态，首先要理解python的数据类型
# 当我们定义一个class时，实际上时定义了一种数据类型，这种数据类型和python自带的数据类型，比如str,list,dict没有什么两样
a = list()  # a是list类型
b = Animal()  # b是Animal类型
c = Dog()  # c是Dog类型
# 判断一个变量是否是某个类型可以用isinstance()判断
print isinstance(a, list)
print isinstance(b, Animal)
print isinstance(c, Dog)
# True
# True
# True
# 看起来a,b,c确实对应着list,Animal,Dog这3种类型
print isinstance(c, Animal)
# True
# 这样看来，c不仅仅是Dog类型，还是Animal类型
# 这是因为Dog是从Animal继承下来的，当我们创建了一个Dog的实例c，我们认为c的数据类型是Dog没错
# 但是c同时是Animal也没错,Dog本来就是Animal的一种
# 所以，在继承关系中，如果一个实例的数据类型是某个子类，那它的数据类型也可以看作是父类，但是反过来是不行的
print isinstance(b, Dog)
# False
# Dog可以看成Animal，但是Animal不能看成Dog
# 要理解多态的好处，还可以再编写一个函数，这个函数接收一个Animal类型的变量
def run_twice(animal):
    animal.run()
    animal.run()
run_twice(Dog())
# Dog is running...
# Dog is running...
# 新增一个Animal的子类
class Turtoise(Animal):
    def run(self):
        print 'Tortoise is running slowly...'
run_twice(Turtoise())
# Tortoise is running slowly...
# Tortoise is running slowly...
# 可以发现，新增一个Animal子类，不必对run_twice()做任何修改
# 实际上，任何依赖Animal作为参数的函数或方法都可以不加修改地正常运行，原因就在于多态
# 多态的好处就是
# 对于一个变量，我们只需要知道它是Animal类型，无需确切地知道它的子类型，就可以放心地调用run()方法
# 而具体调用的run()方法是作用在Animal、Dog、Cat还是Tortoise对象上，由运行时该对象的确切类型决定，这就是多态真正的威力：
# 调用方只管调用，不管细节，而当我们新增一种Animal的子类时，只要确保run()方法编写正确
# 不用管原来的代码是如何调用的。这就是著名的“开闭”原则：
# 对扩展开放：允许新增Animal子类；
# 对修改封闭：不需要修改依赖Animal类型的run_twice()等函数
# 继承还可以一级一级地继承下来，就好比从爷爷到爸爸、再到儿子这样的关系。而任何类，最终都可以追溯到根类object


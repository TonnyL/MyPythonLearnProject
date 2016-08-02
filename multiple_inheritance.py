#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 多重继承
# 继承是面向对象编程的一个重要方式，因为通过继承，子类可以扩展父类的功能
class Animal(object):
    pass

# 大类
class Mammal(Animal):  # 哺乳类
    pass
class Bird(Animal):  # 鸟类
    pass

# 各种动物
class Dog(Mammal):
    pass
class Bat(Mammal):
    pass
class Parrot(Bird):
    pass
class Ostrich(Bird):
    pass

# 给动物加上Runnable和Flyable的功能，只需要先定义好Runnable和Flyable的类
class Runnable(object):
    def run(self):
        print 'Running...'
class Flyable(object):
    def fly(self):
        print 'Flying...'
# 对于需要Runnable功能的动物，就继承一个Runnable,对于需要Flyable的动物，就继承一个Flyable
class Dog(Mammal, Runnable):
    pass
class Parrot(Bird, Flyable):
    pass
# 通过多继承，一个子类可以同时获得多个父类的所有功能


# Mixin
# 在设计类的继承关系时，通常，主线都是单一继承下来的
# 但是，如果需要’混入‘额外的功能，通过多继承就可以实现
# 这种设计模式称之为Mixin
# 为了更好的看出继承关系，我们把Runnable和Flyable改为RunnableMixin和FlyableMixin
class RunnableMixin(object):
    def run(self):
        print 'Running...'
class FlyableMixin(object):
    def fly(self):
        print 'Flying...'

class Dog(Animal, RunnableMixin):
    pass
# Mixin的目的就是给一个类增加多个功能，这样，在设计类的时候，我们会优先考虑通过多重继承来组合实现多个Mixin的功能
# 而不是设计多层次的复杂的继承关系
# python自带的很多库也使用了Mixin
# 例如，python自带的TCPServer和UDPServer这两类网络服务
# 而要同时服务多个用户就必须使用多进程或多线程模型
# 这两种模型由ForkingMixin和ThreadMixin提供
# 通过组合，我们就可以创建出合适的服务来
# 比如，编写一个多进程的TCP服务
# class MyTCPServer(TCPServer, ForkingMixin):
#     pass
# 比如，编写一个多线程的UDP服务
# class MyUDPServer(UDPServer, ThreadMixin):
#     pass

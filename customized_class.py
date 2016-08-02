#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 定制类
# 看到类似__slots__这种形如__xxx__的变量或者函数名就需要注意，在python中是有特殊用途的
# __slots__我们已经知道怎么用了，__len__()方法我们也知道是为了能让class作用于len()函数
# 除此之外，python的class中还有很多这样有特殊用途的函数，可以帮助我们定制类

# __str__
# 我们先定义一个Student类
class Student(object):
    def __init__(self, name):
        self.name = name

print Student('Tony')
# <__main__.Student object at 0x02A780B0>
# 打印出了对象的地址
# 怎样才能打印出更加好看的信息呢？
# 只需要定义好__str__()方法，返回一个好看的字符串就好了
class Student(object):
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return 'Student object (name:%s)' % self.name

s = Student('Tony')
print s
# Student object (name:Tony)
# 同时也可以将调试时使用的方法__repr__()的方法一同写上
class Student(object):
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return 'Student object (name:%s)' % self.name
    __repr__ = __str__


# __iter__
# 如果一个类想被用于for ... in 循环，类似list和tupel那样，就必须实现一个__iter__()方法，该方法返回一个迭代对象
# 然后，python的for循环就会不断调用该迭代对象的next()方法拿到循环的下一个值，直到遇到StopIteration错误时退出循环
# 我们以斐波那契数列为例，写一个Fib类，可以作用于for循环：
class Fib(object):
    def __init__(self):
        self.a, self.b = 0, 1 # 初始化两个计数器a，b

    def __iter__(self):
        return self # 实例本身就是迭代对象，故返回自己

    def next(self):
        self.a, self.b = self.b, self.a + self.b # 计算下一个值
        if self.a > 100: # 退出循环的条件
            raise StopIteration();
        return self.a # 返回下一个值
# 现在，试试把Fib实例作用于for循环：
for n in Fib():
    print n
# 1
# 1
# 2
# 3
# 5
# 8
# 13
# 21
# 34
# 55
# 89


# __getitem__
# Fib实例虽然能作用于for循环，看起来和list有点像，但是，把它当成list来使用还是不行，比如，取第5个元素：
# print Fib()[5]
# TypeError: 'Fib' object does not support indexing
# 要表现得像list那样按照下标取出元素，需要实现__getitem__()方法：
class Fib(object):
    def __getitem__(self, n):
        a, b = 1, 1
        for x in range(n):
            a, b = b, a + b
        return a
# 现在，就可以按下标访问数列的任意一项了：
f = Fib()
print f[0]
print f[1]
print f[2]
# 1
# 1
# 2
# 但是list有个神奇的切片方法：
print range(100)[5:10]
# [5, 6, 7, 8, 9]
# 对于Fib却报错。原因是__getitem__()传入的参数可能是一个int，也可能是一个切片对象slice，所以要做判断：
class Fib(object):
    def __getitem__(self, n):
        if isinstance(n, int):
            a, b = 1, 1
            for x in range(n):
                a, b = b, a + b
            return a
        if isinstance(n, slice):
            start = n.start
            stop = n.stop
            a, b = 1, 1
            L = []
            for x in range(stop):
                if x >= start:
                    L.append(a)
                a, b = b, a + b
            return L
# 现在试试Fib的切片：
f = Fib()
print f[0: 5]
# [1, 1, 2, 3, 5]
# 但是没有对step参数作处理：
print f[:10:2]
# [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# 也没有对负数作处理，所以，要正确实现一个__getitem__()还是有很多工作要做的。
# 此外，如果把对象看成dict，__getitem__()的参数也可能是一个可以作key的object，例如str。
# 与之对应的是__setitem__()方法，把对象视作list或dict来对集合赋值。最后，还有一个__delitem__()方法，用于删除某个元素。
# 总之，通过上面的方法，我们自己定义的类表现得和Python自带的list、tuple、dict没什么区别
# 这完全归功于动态语言的“鸭子类型”，不需要强制继承某个接口。


# __getattr__
# 正常情况下，当我们调用类的方法或属性时，如果不存在，就会报错。比如定义Student类：
class Student(object):

    def __init__(self):
        self.name = 'Tony'
# 调用name属性，没问题，但是，调用不存在的score属性，就有问题了：
s = Student()
print s.name
# TOny
# print s.score  AttributeError: 'Student' object has no attribute 'score'
# 错误信息很清楚地告诉我们，没有找到score这个attribute。
# 要避免这个错误，除了可以加上一个score属性外，Python还有另一个机制，那就是写一个__getattr__()方法，动态返回一个属性
# 修改如下：
class Student(object):

    def __init__(self):
        self.name = 'Tony'

    def __getattr__(self, attr):
        if attr=='score':
            return 99
# 当调用不存在的属性时，比如score，Python解释器会试图调用__getattr__(self, 'score')来尝试获得属性
# 这样，我们就有机会返回score的值：
s = Student()
print s.score
# 99
# 返回函数也是完全可以的：
class Student(object):

    def __getattr__(self, attr):
        if attr=='age':
            return lambda: 25
# 只是调用方式要变为：
s = Student()
print s.age()
# 25
# 注意，只有在没有找到属性的情况下，才调用__getattr__，已有的属性，比如name，不会在__getattr__中查找。
# 此外，注意到任意调用如s.abc都会返回None，这是因为我们定义的__getattr__默认返回就是None
# 要让class只响应特定的几个属性，我们就要按照约定，抛出AttributeError的错误：
class Student(object):

    def __getattr__(self, attr):
        if attr=='age':
            return lambda: 25
        raise AttributeError('\'Student\' object has no attribute \'%s\'' % attr)

# 这实际上可以把一个类的所有属性和方法调用全部动态化处理了，不需要任何特殊手段。
# 这种完全动态调用的特性有什么实际作用呢？作用就是，可以针对完全动态的情况作调用。


# __call__
# 一个对象实例可以有自己的属性和方法，当我们调用实例方法时，我们用instance.method()来调用
# 能不能直接在实例本身上调用呢？类似instance()？在Python中，答案是肯定的。
# 任何类，只需要定义一个__call__()方法，就可以直接对实例进行调用。请看示例：
class Student(object):
    def __init__(self, name):
        self.name = name

    def __call__(self):
        print('My name is %s.' % self.name)
# 调用方式如下：
s = Student('Tony')
s()
# My name is Tony.
# __call__()还可以定义参数
# 对实例进行直接调用就好比对一个函数进行调用一样，所以你完全可以把对象看成函数，把函数看成对象
# 因为这两者之间本来就没啥根本的区别
# 如果你把对象看成函数，那么函数本身其实也可以在运行期动态创建出来，因为类的实例都是运行期创建出来的
# 这么一来，我们就模糊了对象和函数的界限
# 那么，怎么判断一个变量是对象还是函数呢？
# 其实，更多的时候，我们需要判断一个对象是否能被调用，能被调用的对象就是一个Callable对象
# 比如函数和我们上面定义的带有__call()__的类实例：
print callable(Student('Tony'))
print callable(max)
print callable([1, 2, 3])
print callable(None)
# True
# True
# False
# False
# 通过callable()函数，我们就可以判断一个对象是否是“可调用”对象。

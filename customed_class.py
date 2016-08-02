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



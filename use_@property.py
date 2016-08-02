#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 使用@property
# 在绑定属性时，如果我们直接把属性暴露出去，虽然写起来简单，但是，没办法检查参数，导致可以把成绩随便改
# s = Student()
# s.score = 9999
# 这显然不符合逻辑。为了限制score的范围，我们可以通过一个set_score()方法，在通过一个get_score()方法获取成绩
# 这样，在set_score()方法里，就可以检查参数
class Student(object):
    def get_score(self):
        return self._score
    def set_score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value
# 现在，对任意的Student实例进行操作，就不能随心所欲的设置score了
s = Student()
s.set_score(60)
print s.get_score()
# s.set_score(101)  ValueError: score must between 0 ~ 100!
# 但是，上面的调用方法又略显复杂，没有直接调用属性这么简单
# 有没有既能检查参数，又能用类似属性这样简单的方法来访问类的变量呢？
# python内置的@property装饰器就是负责把一个方法变成属性调用的
class Student(object):
    @property
    def score(self):
        return self._score
    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value
# @property的实现比较复杂，我们先考虑如何使用
# 把一个getter方法变成属性，只需要加上@property就可以了
# 此时，@property本身又创建了另一个装饰器@score.setter，负责把一个setter方法变成属性赋值
# 于是我们就拥有了一个可控的属性操作
s = Student()
s.score = 60  # OK，实际转化为s.set_score(60)
print s.score  # OK，实际转化为s.get_score()
# 60
# s.score = 101  ValueError: score must between 0 ~ 100!
# 注意到这个神奇的@property，我们对属性操作的时候，就知道该属性可能不是直接暴露的，而是通过setter和getter方法来实现的
# 还可以定义只读属性，之定义getter方法，不定义setter方法就是一个只读属性

#!/usr/bin/env python
# -*- coding: utf-8 -*-

from types import MethodType

# 使用__slots__
# 正常情况下，当我们定义了一个class，创建了一个class的实例后
# 我们可以给该实例绑定任何属性和方法，这就是动态语言的灵活性
class Student(object):
    pass
# 然后尝试给实例绑定一个属性
stu = Student()
stu.name = 'Mike'
print stu.name
# Mike
# 还可以尝试给实例绑定一个方法
def set_age(self, age):
    self.age = age
stu.set_age = MethodType(set_age, stu, Student)
stu.set_age(25)
print stu.age
# 25
# 但是，给一个实例绑定的方法，对另一个实例是不起作用的
# s2 = Student()  # 创建新的实例
# s2.set_age(25)  # 尝试调用方法
# AttributeError: 'Student' object has no attribute 'set_age'

# 为了给所有的实例绑定方法，所有实例均可调用
def set_score(self, score):
    self.score = score

Student.set_score = MethodType(set_score, None, Student)

# 给class绑定方法后，所有实例均可调用
stu.set_score(60)
print stu.score
stu2 = Student()
stu2.set_score(60)
print stu2.score
# 60
# 60
# 通常情况下，上面的set_score()方法可以定义在class中，但是动态绑定允许我们在程序运行过程中动态给class加上功能


# 使用__slots__
# 但是，如果我们想要限制class的属性怎么办？
# 比如，只允许对Student实例添加name，age属性
# 为了达到限制目的，python允许在定义class的时候，定义一个特殊的__slots__变量，来限制该class能添加的属性
class Student(object):
    __slots__ = ('name', 'age')  # 用tuple定义允许绑定的属性名称
s = Student()
s.name = 'Neo'
s.age = 20
# s.score = 99  # AttributeError: 'Student' object has no attribute 'score'
# 绑定属性score
print s.name
print s.age
# Neo
# 20
# print s.score
# 由于'score'没有放到__slots__中，所以不能绑定score属性，试图绑定score将会得到AttributeError
# 使用__slots__需要注意，__slots__定义的属性仅对当前类起作用，对继承的子类是不起作用的
# 除非在子类中也定义__slots__，这样，子类允许定义的属性就是自身的__slots__加上父类的__slots__

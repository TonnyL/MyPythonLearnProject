#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 访问限制
# 在class内部，可以有属性和方法，而外部代码可以通过直接调用实例变量的方法来操作数据，这样就隐藏了内部的复杂逻辑
# 但是，从Student类定义来看，外部代码还是可以自由修改一个实例的name,score属性
class Student(object):

    def __init__(self, name, score):
        self.name = name
        self.score = score

    def print_score(self):
        print '%s: %s' % (self.name, self.score)

    def get_score(self):
        if self.score >= 90:
            return 'A'
        elif self.score >= 60:
            return 'B'
        else:
            return 'C'

George = Student('George', 60)
print George.score
George.score = 61
print George.score
# 60
# 61
# 如果要让内部属性不被外部访问，可以把属性的名称前面加上两个下划线__，在python中，实例的变量名如果以__开头，就变成了一个私有变量
# 只有内部可以访问，外部不能访问
class Student(object):

    def __init__(self, name, score):
        self.__name = name
        self.__score = score

    def print_score(self):
        print '%s: %s' % (self.__name, self.__score)

    def get_score(self):
        if self.__score >= 90:
            return 'A'
        elif self.__score >= 60:
            return 'B'
        else:
            return 'C'

# 改完后，对于外部代码来说，没什么变动，但是已经无法从外部访问变量.__name和变量.__score了
# Larry = Student('Larry', 60)
# print Larry.__name
# AttributeError: 'Student' object has no attribute '__name'
# 这样就确保了外部代码不能随意访问修改对象内部的状态，这样通过访问限制的保护，程序的健壮性更强了
# 但是如果外部代码要获取name和score怎么办？可以给类增加get_score和get_name这样的方法
class Student(object):

    def __init__(self, name, score):
        self.__name = name
        self.__score = score

    def print_score(self):
        print '%s: %s' % (self.__name, self.__score)

    def get_score(self):
        return self.__score

    def get_name(self):
        return self.__name

    def set_name(self, name):  # setter of name
        self.__name = name

    def set_score(self, score):  # setter of score
        self.__score = score

# 如果又要允许外部代码修改name和score呢？添加setter
# setter of name and score above

# 原先通过实例变量修改属性的形式也可以啊，为什么要通过setter呢？
# 因为在方法中，可以对参数做检查，避免传入无效的参数
# def set_score(self, score):
#     if 0 <= score <= 100:
#         self.__score = score
#     else:
#         raise ValueError('bad score')
# 需要注意的是，在python中，变量名类似__xxx__也可以是双下划线结尾的，是特殊变量，特殊变量是可以直接访问的
# 不是private变量，所以，不能用__score__,__name__这样的变量名
# 有些时候，会看到以一个下划线开头的实例变量名，比如_name，这样的实例变量外部是可以访问的，但是，按照约定俗成的规矩
# 当你看到这样的变量时，意思是，虽然我可以被访问，但是，请把我视为私有变量，不要随意访问
# 双下划线开头的变量是不是一定不能从外部访问呢？其实也不是
# 不能直接访问__name是因为python解释器把__name变量改成了_Student__name，所以，仍然可以通过_Student__name来访问__name变量
print Student('Lucas', 60)._Student__name
# Lucas
# 但是强烈建议不这么做，因为不同版本的python解释器可能会把__name改成不同的变量名
# 总的来说，python本身没有任何强制机制阻止你干坏事，一切全靠自觉

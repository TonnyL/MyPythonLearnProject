#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 面向对象最重要的就是类(Class)和实例(Instance)，必须牢记类是抽象的模板，比如student类，而实例是根据类创建出来的一个个的‘对象’
# 每个对象都拥有相同的方法，但各自的数据可能不同
# 以student类为例，在python中，定义类是通过关键字class：
class Student(object):
    pass
# class后面紧接着类名，即Student，类名通常是大写开头的单词，紧接着是(object),表示该类是从哪个类继承下来
# 通常，如果没有合适的继承类，就使用object类，这是所有类最终都会继承的类
# 定义好Student类后，就可以根据Student类创建出Student的实例，创建实例是通过类名+()实现：
stu = Student()
print stu
print Student
# <__main__.Student object at 0x02A08050>
# <class '__main__.Student'>

# 可以看到，变量stu指向的是一个Student的object，后面的内容是其内存地址，每个object的地址都不相同，而Student本身就是一个类
# 可以自由的给一个实例变量绑定属性，比如，给stu绑定一个name属性
stu.name = 'Allen'
print stu.name
# Allen
# 由于类可以起到模板的作用，因此，可以在创建实例的时候，把我们认为必须绑定的属性强制填写进去
# 通过定义一个特殊的__init__方法，在创建实例的时候，就把name，score等属性绑上去
class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score
# 注意到__init__方法的第一个参数永远是self，表示创建的实例本身
# 因此，在__init__方法内部，就可以把各种属性绑定到self，因为self就指向创建的实例本身
# 有了__init__方法，在创建实例的时候，就不能传入空的参数了
# 必须传入与__init__方法匹配的参数，但self不需要传，python解释器会自己把实例变量传进去
allen = Student('Allen', 60)
print allen.name
print allen.score
# Allen
# 60
# 和普通的函数相比，在类中定义的函数只有一点不同，就是第一个参数永远是实例变量self
# 并且，调用时，不用传递该参数
# 除此之外，类的方法和普通函数没有什么区别，所以，仍然可以用默认参数，可变参数和关键字参数


# 数据封装
# 面向对象编程的另外一个重要特点就是数据封装
# 在上面的Student类中，每个实例就拥有各自的name和score这些数据
# 我们可以通过函数来访问这些数据，比如打印一个学生的成绩
def print_score(std):
    print '%s: %s' % (std.name, std.score)
print_score(allen)
# Allen: 60

# 但是，既然Student实例本身就拥有这些数据，要访问这些数据，就没有必要从外面的函数访问，可以直接在Student类的内部定义访问数据的函数
# 这样，就把数据封装起来了
# 这些封装数据的函数是和Student类本身关联起来的，我们成为类的方法
class Student(object):

    def __init__(self, name, score):
        self.name = name
        self.score = score

    def print_score(self):
        print '%s: %s' % (self.name, self.score)

# 要定义一个方法，除了第一个参数是self外，其他和普通函数一样
# 要调用一个方法，只需要在实例变量上直接调用，除了self不用传递，其他参数正常传递
Student('Zack', 60).print_score()
# Zack: 60
# 这样一来，我们从外部看Student类，就只需知道，创建实例需要给出name, score，而如何打印的，都是在Student类内部定义的
# 这里数据和逻辑都被封装起来了，调用很容易，但却不用知道内部实现的细节

# 封装的另一个好处就是给Student类增加新的方法，比如get_score:
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
# 同样的，get_grade()方法可以直接在实例变量上调用，不需要知道内部实现细节
print Student('Harry', 60).get_score()
# B


# 小结
# 和静态语言不同，python允许对实例变量绑定任何数据
# 也就是说，对于两个实例变量，虽然他们都是同一个类的不同实例，但是拥有的变量名称可能不同

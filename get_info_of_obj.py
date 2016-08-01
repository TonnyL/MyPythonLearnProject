#!/usr/bin/env python
# -*- coding: utf-8 -*-

from inheritance_and_polymorphism import Animal
import types

# 获取对象信息
# 当我们拿到一个对象的引用时，如何知道这个对象是什么类型，有哪些方法呢？

# 使用type()
# 首先，来判断对象类型，使用type()函数
print type(123)
print type('str')
print type(None)
# <type 'int'>
# <type 'str'>
# <type 'NoneType'>

# 如果一个变量指向函数或者类，也可以用type()判断
print type(abs)
a = Animal()
print type(a)
# <type 'builtin_function_or_method'>
# <class 'inheritance_and_polymorphism.Animal'>
# 但是type()函数返回的是什么类型呢？它返回type类型
# 如果我们要在if语句中判断，就需要比较两个变量的type类型是否相同
print type(type)
# <type 'type'>
print type(123) == type(456)
print type('123') == type('str')
print type('str') == type(123)
# True
# True
# False
# 但是这种写法太麻烦，python把每种type类型都定义好了常量，放在types模块里面，使用之前，需要先导入
print type('str') == types.StringType
print type(u'str') == types.UnicodeType
print type([]) == types.ListType
print type(str) == types.TypeType
# True
# True
# True
# True
# 注意最后一种类型，TypeType，所有类型本身的类型就是TypeType
# 例如
print type(int) == type(str) == types.TypeType
# True


# 使用isinstance()
# 对于class的继承关系来说，使用type()就很不方便，我们要判断class的类型，可以使用isinstance()函数
# isinstance()的用法在inheritance_and_polymorphism.py中已经提到，这里只看一些高级一点的用法
print isinstance('a', (str, unicode))
print isinstance(u'a', (str, unicode))
# True
# True
# 由于str和unicode都是从basestring继承下来的，所以，上面的代码也可以改为
print isinstance(u'a', basestring)
# True


# 使用dir()
# 如果要获取一个对象的所有属性和方法，可以使用dir()函数，它返回一个包含字符串的list
print dir('A')
# ['__add__', '__class__', '__contains__', '__delattr__', '__doc__', '__eq__', '__format__',
# '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__getslice__', '__gt__', '__hash__',
#  '__init__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__',
# '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__',
# '__subclasshook__', '_formatter_field_name_split', '_formatter_parser', 'capitalize', 'center', 'count',
#  'decode', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'index', 'isalnum', 'isalpha', 'isdigit',
# 'islower', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'partition', 'replace',
# 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip',
# 'swapcase', 'title', 'translate', 'upper', 'zfill']

# 类似__xxx__的属性和方法在python中是有特殊用途的，比如__len__方法返回长度
# 在python中，如果你调用len()函数试图获取一个对象的长度，实际上，在len()函数的内部，它自动去调用该对象的__len__方法
# 所以，下面的代码是等价的
print len('ABC')
print 'ABC'.__len__()
# 3
# 3

# 我们自己写的类，如果也想使用len()方法，就自己写一个__len__()方法
class MyLenClass(object):
    def __len__(self):
        return 10

obj = MyLenClass()
print len(obj)
# 10
# 剩下的都是普通属性或者方法，比如lower()返回小写的字符串
# 仅仅把属性和方法列出来是不够的，配合getattr(),setattr(),hasattr()，我们可以直接操作一个对象的状态
class MyObj(object):
    def __init__(self):
        self.x = 9
    def power(self):
        return self.x * self.x
o = MyObj()
# 紧接着，可以测试该对象的属性
print hasattr(o, 'x')  # 有属性'x'吗
print hasattr(o, 'y')  # 有属性'y'吗
setattr(o, 'y', 19)  # 添加属性'y'，值为19
print hasattr(o, 'y')  # 有属性'y'吗
print getattr(o, 'y')  # 获取属性'y'的值
print o.y
# True
# False
# True
# 19
# 19

# 如果试图获取不存在的属性，会抛出AttributeError的错误
# 可以传入一个默认参数，如果属性不存在，就返回默认值
getattr(o, 'z', 404)  # 获取属性'z'，如果不存在，返回默认值404
# 也可以获取对象的方法
print hasattr(o, 'power')
# True
fn = getattr(o, 'power')
print fn()
# 81



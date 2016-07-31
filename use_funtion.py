# -*- coding:utf-8 -*-

# 调用函数
# python内置了很多的函数，可以直接调用
# 要调用一个函数，需要知道函数的函数名和参数，比如求绝对值的函数abs(),只有一个参数
print abs(1)
print abs(-1)
print abs(-1.1)
# print abs(1, 1)
# 调用函数时，如果传入的参数数量不对，就会报TypeError的错误，并且python会告诉你，abs()有且极有一个参数
# 如果传入的参数数量是正确的，但是参数类型不正确的话，也会报TypeError的错误
# 而比较函数cmp(x,y)就需要两个函数，如果x<y ，返回-1，如果x==y，返回0，如果x>y，返回-1
print cmp(1, 2)
print cmp(1, 1)
print cmp(2, 1)


# 数据类型转换
print int('12')
print int(12.1)
print float(1)
print float('2.1')
print bool(1)
print bool(0)
print bool('True')
print unicode(100)

# 函数名其实是指向一个函数的引用，完全可以把函数名赋值给一个变量，相当于给这个函数起了一个别名
absolute = abs
print absolute(-1)

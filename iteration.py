# -*- coding:utf-8 -*-

# 迭代
# 如果给定一个list或者tuple，我们可以通过for循环遍历这个list或者tuple，这种便利成为迭代
# list这种数据类型虽然有下标，但很多其他数据类型是没有下标的
# 但是，只要是可迭代对象，都可以迭代
# 例如
dic = {'a': 1, 'b': 2, 'c': 3}
for key in dic:
    print 'key=', key
# 有可能结果并不是按照a,b,c的顺序出现，这是因为在dict内部，数据的存放顺序并不是按存放顺序存放的
# 默认情况下，dict迭代的是key，如果要迭代value，
for value in dic.itervalues():
    print 'value=', value
# 如果要同时迭代key和value，可以
for k, v in dic.iteritems():
    print 'key->', k, 'value-->', v

# 由于字符串也是可迭代对象，所以也可以用for循环
for char in 'ABC':
    print char
# 所以，当我们使用for循环时，只要作用于一个可迭代对象，for循环就可以正常运行，而我们不关心该对象究竟是list类型还是其他类型
# 但是我们要怎样判断一个对象是否可以迭代呢？
# 方法是通过collections模块的Iterable类型判断
from collections import Iterable
print isinstance('ABC', Iterable)
print isinstance([1, 2, 3], Iterable)
print isinstance((1, 2, 3), Iterable)
print isinstance(123, Iterable)

# 如果要对list实现类似java那样的下标循环，应该怎样实现呢？
# python内置的enumerate()函数，可以把list变成索引-元素树，这样就可以在for循环中同时迭代元素索引和元素本身了
for index, value in enumerate(['A', 'B', 'C']):
    print index, value
# 上面的for循环中，同时引用了两个变量，类似于下面的代码：
for x,y in [(1, 'a'), (2, 'b'), (3, 'c')]:
    print 'x->', x, 'y->', y

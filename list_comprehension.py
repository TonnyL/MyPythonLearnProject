# -*- coding:utf-8 -*-

# 列表生成式
# 利用列表生成式可以创建list
# 如果要生成list:[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]可以用range(1,11)
L = range(1, 11)
print L
# 但如果要生成[1x1, 2x2, 3x3, ..., 10x10],应该怎么做呢？
# 方法1.循环
L = []
for x in range(1, 11):
    L.append(x*x)
print L
# 循环的方法太繁琐，另一种简单的方法
# 方法2.列表生成式
L = [x*x for x in range(1, 11)]
print L
# 将要生成的元素放在前面，后面跟for循环就可以把list创建出来
# 添加判断条件还可以筛选出偶数的平方和
print [x*x for x in range(1, 11) if x % 2 == 0]
# 还可以使用两层循环
print [x + y for x in 'ABC' for y in '123']
# for循环可以同时迭代两个甚至多个变量，列表生成式也可以使用两个变量生成list
L = {'k1': 'v1', 'k2': 'v2'}
print ['key-->' + key + 'value-->' + value for key, value in L.iteritems()]

L = ['Hello', 'World', 18, 'Apple', None]
print [value.lower() for value in L if isinstance(value, str)]

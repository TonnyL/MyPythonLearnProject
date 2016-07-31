# -*- coding:utf-8 -*-

# 高阶函数
# 变量可以指向函数
# 以python内置的求绝对值的函数abs()为例，调用该函数用以下代码
print abs(-10)
# 但是如果只写abs呢
print abs
# 可见，abs(-10)是函数调用，而abs是函数本身
# 要获得函数调用的结果，可以把结果赋值给变量
a = abs(-10)
print a
# 但是，如果把函数本身赋值给变量呢？
f = abs
print f
# 结论，函数本身也可以赋值给变量，即，变量可以指向函数
# 如果一个变量指向了一个函数，那么，是否可以通过变量调用这个函数呢？
# 答案是肯定的。在use_function.py的最后，我们将abs赋值给了变量absolute，通过absolute成功实现了abs函数的功能

# 函数名也是变量
# 那么函数名是什么呢？函数名其实就是指向函数的变量！
# 对于abs()这个函数，完全可以把函数名abs看成变量，它指向一个可以计算绝对值的函数
# 如果把abs指向别的对象，会发生什么呢？
# abs = 10
# print abs(-10)
# TypeError: 'int' object is not callable
# 把abs指向10后，就无法通过abs(-10)调用该函数了！
# 要恢复abs()函数，需要重启python环境！

# 传入函数
# 既然变量可以指向函数，函数的参数能接受变量，那么一个函数就可以接受其他函数作为参数，这种函数就成为高阶函数
# 一个最简单的高阶函数
def add(x, y, f):
    return f(x) + f(y)
print add(-1, 2, abs)



# map / reduce
# python内建了map()和reduce()函数
# 我们先看map。map()函数接收两个参数，一个是函数，一个是序列，map将传入的函数依次作用到序列的每个元素，并把结果作为新的list返回。
# 举例说明，比如我们有一个函数f(x)=x2，要把这个函数作用在一个list [1, 2, 3, 4, 5, 6, 7, 8, 9]上，就可以用map()实现如下：
def f(x):
    return x * x
print map(f, [1, 2, 3, 4, 5])
# map作为高级函数，事实上它把运算规则抽象了，因此，我们不但可以计算f(x)=x*x，还可以计算任意复杂的函数
# 比如，把这个list所有数字转换为字符串
print map(str, [1, 2, 3, 4, 5])
# 转换为float
print map(float, [1, 2, 3, 4, 5])

# 再看reduce的用法
# reduce把一个函数作用于一个序列[x1, x2, x3...]上，这个函数必须接收两个参数，reduce把结果和序列的下一个元素做累计运算
# reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)
# 比如一个序列求和
def add(x, y):
    return x+y

print reduce(add, [1, 2, 3, 4, 5])

# 考虑到字符串str也是一个序列，对上面的例子稍加修改，配合map()，我们就可以写出str转换为int的函数
def fn(x, y):
    return x * 10 + y
def char2num(s):
    return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]

print reduce(fn, map(char2num, '123456'))
# print reduce(fn, map(int, '123456'))
# 整理成一个str2int()函数就是
def str2int(s):
    def fn1(x, y):
        return x * 10 + y
    def char2num1(s):
        return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]
    return reduce(fn1, map(char2num1, s))
print str2int('123456')


# 练习
# 利用map()函数，把用户输入的不规范的英文名字，变为首字母大写，其他小写的规范名字。
# 输入：['adam', 'LISA', 'barT']，输出：['Adam', 'Lisa', 'Bart']。
def func(names):
    def format_one_name(L):
        for k, v in enumerate(L):
            if k == 0:
                n = v.upper()
            else:
                n += v.lower()
        return n
    names_formatted = []
    for i in names:
        names_formatted.append(format_one_name(map(str, i)))
    return names_formatted

print func(['adam', 'LISA', 'barT'])

# 请编写一个prod()函数，可以接受一个list并利用reduce()求积
def prod(l):
    def fn(x, y=1):
        return x * y
    return reduce(fn, l)

print prod([1])


# filter
# python内建的filter()函数用于过滤序列
# 和map()类似，filter也接收一个函数和一个序列。和map()不同的时，filter把传入的函数依次作用鱼每个元素
# 然后根据返回值是True还是False决定是否丢弃该元素
# 例如在一个list中，删掉偶数，只保留奇数
def is_odd(n):
    return n % 2 == 1

print filter(is_odd, [1, 2, 3, 4, 5, 6])
# 如果要把str中的空字符删掉
def not_empty(s):
    return s and s.strip()
print filter(not_empty, map(str, 'A B cDEF'))

# 练习
# 请尝试用filter()删除1~100的素数。
def is_not_prime_number(num):
    if num == 1:
        return 1
    for i in range(2, num - 1):
        if num % i != 0:
            return num

print filter(is_not_prime_number, range(1, 101))


# -*- coding:utf-8 -*-

# 由于函数也是一个对象，而且函数对象可以赋值给变量，所以，通过变量也能调用该函数
def now():
    print '2016-07-31'
f = now
f()

# 函数对象有一个_name_属性，可以拿到函数的名字
print f.__name__
print now.__name__

# 现在，假设我们要增强now()函数的功能，比如，在now()函数调用前后自动打印日志，但又不希望修改now()函数的定义
# 这种在代码运行期间动态增加功能的方式，称之为‘装饰器’
# 事实上，decorator就是一个返回函数的高阶函数。所以，我们要定义一个能打印日志的decorator，定义如下
def log(func):
    def wrapper(*args, **kwargs):
        print 'call %s():' % func.__name__
        return func(*args, **kwargs)
    return wrapper
# 观察上面的log，因为他是一个decorator，所以接受一个函数作为参数，并返回一个参数。
# 我们要借助python的@语法，把decorator置于函数的定义处

@log
def fun():
    print 'function test'

# 调用fun()函数，不仅会运行now()函数本身，还会在运行now()函数前打印一行日志
fun()
# 把@log放到now()函数定义处，相当于执行了语句：
# now = log(now)
# 由于log()是一个decorator，返回一个函数，所以，原来的now()函数仍然存在，只是现在同名的now变量指向了新的函数，于是调用now()将执行新函数
# 即在log()函数中返回的wrapper()函数
# wrapper()函数的参数定义是(*args, **kwargs),因此，wrapper()函数可以接受任意参数的调用
# 如果decorator本身需要传入参数，那就需要编写一个返回decorator的高阶函数，写出来会更复杂
def log(text):
    def decorator(func):
        def wrapper(*args, **kwargs):
            print '%s %s' % (text, func.__name__)
            return func(*args, **kwargs)
        return wrapper
    return decorator

@log('execute')
def fun():
    print 'function test'
fun()
# 和两层嵌套的decorator相比，3层嵌套的效果为：
# fun = log('execute')(fun)
# 首先执行log('execute'),返回的是decorator函数，再调用返回的函数，参数是fun函数，最终调用wrapper函数
print fun.__name__
# 经过decorator装饰后的函数，函数名已经变成了wrapper
# 所以，需要把原始函数的__name__等属性复制到wrapper中，否则，有些依赖函数签名的代码执行就会出错
import functools
def log(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print 'start call %s()' % func.__name__
        func(*args, **kwargs)
        print 'end call %s()' % func.__name__
    return wrapper


# -*- coding:utf-8 -*-

# 函数的参数
# 定义函数的时候，我们把参数的名字和位置记录下来，函数的接口定义就算完成了
# 对于函数的调用者来说，只需要知道传递正确的参数，以及函数的返回值是什么样的就可以了
# 函数内部复杂的逻辑被封装，使用者无需了解

# python的函数定义十分简单，但是灵活度也非常大
# 除了正常定义的必选参数外，还可以使用默认参数、可变参数和关键字参数
# 这使得函数定义出来的接口，不但能处理复杂的参数，还能简化调用者的代码

# 默认参数
def power(x):
    return x*x
# 调用power()函数时，必须传入有且仅有的一个参数x
print power(2)
# 如果要计算x的立方应该怎么办？可以再定义一个power3()函数，但是如果要计算更多次方呢？
# 我们可以把power(x)修改为power(x,n)用于计算x的n次方
def power(x, n):
    amount = 1
    while n > 0:
        n -= 1
        amount = amount * x
    return amount
# print power(2)
# 旧的代码调用失败了，因为我们新增了一个参数导致旧的代码无法正常调用了
# 这时，默认参数就派上用场了。因为我们需要经常计算x的平方，所以完全可以把第二个参数n的默认值设定为2
def power_with_default(x, n=2):
    amount = 1
    while n > 0:
        n -= 1
        amount = amount * x
    return amount

print power_with_default(2)
print power_with_default(2, 3)

# 从上面的例子可以看出，默认参数可以简化函数的调用。
# 设置默认参数需要注意：
# 1.必选参数必须在默认参数之前，否则python的解释器就会报错，为什么？
# 因为python无法确定，传入的参数是已经作为默认参数对应的参数还是其他的参数，产生了歧义
# 例如：
# def power_with_default(n=2, x, another_param):
#     amount = 1
#     while n > 0:
#         n -= 1
#         amount = amount * x
#     return amount
# 调用:power_with_default(2,1)
# 解释器无法确定传入的参数是作为(x, another_param)还是(n, x)还是(n, another_param)，产生了歧义
# 2.如何设置默认参数
# 当函数有多个参数时，变化大的参数放在前面，变化小的参数放后面。变化小的参数可以作为默认参数。
# 使用默认参数最大的好处就是可以降低调用函数的难度
# eg:
def enroll(name, gender):
    print 'name:', name
    print 'gender:',gender
# 这样调用enroll()的时候只需要传入两个参数
enroll('Tony', 'Male')
# 如果要继续传入年龄，城市等信息怎么办？
# 我们可以把年龄，城市等设为默认参数
def enroll(name, gender, age=10, city='Beijing'):
    print 'name:', name
    print 'gender:', gender
    print 'age:', age
    print 'city', city

enroll('Tony', 'Male')
# 这样，调用函数时就只需要修改和默认参数不符的参数的值了
# 可见，默认参数降低了函数调用的难度，而一旦需要更复杂的调用时，又可以传递更多的参数来实现。
# 无论是简单调用还是复杂调用，函数都只需要定义一个

# 有多个默认参数，调用时既可以按顺序提供默认参数，比如调用enroll('Tony', 'Male', 20)
# 意思是，除了name，gender这两个参数外，最后一个参数应用在age上，city参数由于没有提供，使用默认值
# 也可以不按顺序提供部分默认参数。当不按顺序调用时，需要把参数名写上。
# 比如调用enroll('Tony', 'Male', city='Changsha')
# 意思是，city参数使用传递的值，其他默认参数继续使用默认参数

# 默认参数很有用，但是使用不当，也会有大坑
# 先定义一个函数，传入一个list，添加一个end再返回
def add_end(L=[]):
    L.append('end')
    return L
# 使用默认参数时，一开始结果也是对的
print add_end()
# 当你正常调用时，结果似乎不错
print add_end([1, 2, 3])
# 但是，再次调用add_end()时，结果就不对了
print add_end()
print add_end()
# 每次调用都会在后面追加，函数似乎记住了上次添加了'end'的list
# 解释如下：
# python函数在定义时，默认参数L的值就被计算出来了，即[]
# 因为默认参数L也是一个变量，它指向对象[]，每次调用该函数，如果改变了L的内容，则下次调用时默认参数的内容就变了，不再是函数定义时的[]了
# 所以，定义默认参数一定要记住一点：默认参数必须指向不变对象
# 修改上面的例子
def add_end(L=None):
    if L is None:
        L = []
    L.append('end')
    return L
# 现在，无论调用多少次，都不会有问题
print add_end()
print add_end()

# 为什么要设计string、None这样的不可变对象呢？
# 因为不变对象一旦创建，对象内部的数据就不能修改，这样就减少了由于修改数据导致的错误
# 此外，由于对象不变，多任务环境下同时读取对象不需要加锁，同时读没有一点问题

# 可变参数
# 在python函数中，还可以定义可变参数
# 给定一组数字a，b，c……，请计算a2 + b2 + c2 + ……
# 要定义这个函数，我们必须确定要输入的参数，由于参数不确定，我们首先可以想到可以把a,b,c...等作为一个list或者tuple传进来
# 可以定义为
def calculate(numbers):
    summary = 0
    for i in numbers:
        summary = summary + i*i
    return summary
# 但是调用时，需要组装一个list或者tuple
num = [1, 2, 3]
print calculate(num)
# 如果利用可变参数，可以把函数的参数改为可变参数
def calculate(*numbers):
    summary = 0
    for i in numbers:
        summary = summary + i*i
    return summary
print calculate(1, 2, 3)
print calculate()
# 如果已经有一个list或者tuple，要调用一个可变参数，怎么办？
calculate(num[0], num[1], num[2])
# 这样的写法有写繁琐，python允许在list或者tuple前加一个*，把list或者tuple的元素作为可变参数传入
print calculate(*num)

# 关键字参数
# 可变参数允许你传入0个或者多个参数，这些可变参数在调用时自动组装成一个tuple
# 而关键字参数允许你传入0个或任意个含参数名的参数，这些关键字在函数内部自动组装成一个dict
def person(name, age, **kw):
    print 'name:', name, 'age', age, 'other', kw
# 函数person()除了必选参数name,age外，还可以接受关键字参数kw
# 调用函数时，可以只传入必选参数
person('Tony', 1)
# 也可以传入任意个数的关键字参数
person('Mark', 2, city='Changsha')
# 关键字参数有什么用？它可以扩展函数的功能
# 例如在person()函数中，我们保证能接收到name和age这两个参数
# 但是，如果调用者愿意提供更多的参数，也能够接收到
# 和可变参数类似，可以先组装一个dict，然后把这个dict作为参数传入
m_dict = {'city': 'Changsha', 'job': 'Student'}
person('Kiki', 2, city=m_dict['city'], job=m_dict['job'])
# 简化的写法
person('Kiki', 2, **m_dict)

# 参数组合
# 在python中定义函数，可以用必选参数、默认参数、可变参数和关键字参数，这4中参数都可以一起使用，或者只使用其中某些
# 但是注意，参数定义的顺序必须是：必选参数、默认参数、可变参数和关键字参数
# 例如
def func(a, b, c=0, *args, **kw):
    print 'a=', a, 'b=', b, 'c=', c, 'args=', args, 'kw', kw
# 函数调用时，python解释器会自动按照参数位置和参数名把对应的参数传进去
func(1, 2)
func(1, 2, 3)
func(1, 2, 3, 'a', 'b')
func(1, 2, 3, 'a', 'b', key='value')
# 通过一个tuple和dict，也可以调用func
args = {'a', 'b'}
kvargs = {'key': 'value'}
func(*args, **kvargs)
# 所以对于任意函数，对于任何函数，都可以通过类似func(*args, **kvargs)的形式调用，无论它的参数是如何定义的

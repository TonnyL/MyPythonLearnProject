# -*- coding:utf-8 -*-

# 返回函数
# 高阶函数除了可以接受函数作为参数外，还可以把函数作为结果返回
# 我们来实现一个可变参数的求和。通常情况下，求和的函数是这样定义的
def calc_sum(*args):
    ax = 0
    for n in args:
        ax = ax + n
    return ax

# 但是，如果不需要立即求和，而是在后面的代码中，根据需要计算怎么办？可以不返回求和的结果，而是返回求和的函数
def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax
    return sum

# 当我们调用lazy_sum()时，返回的并不是求和结果，而是求和函数
f = lazy_sum(1, 2, 4, 6, 8)
print f
print f()

# 在这个例子中，我们在函数lazy_sum()中又定义了函数sum()，并且，内部函数sum()可以引用外部函数lazy_sum()的参数和局部变量
# 当lazy_sum()返回函数sum()时，相关参数和变量保存在返回的函数中，这种称为“闭包”的程序结构拥有极大的威力

# 请再注意一点，我们在调用函数lazy_sum()时，每次调用都会返回一个新的函数，即使传入相同的参数
f1 = lazy_sum(1)
f2 = lazy_sum(1)
print f1 == f2
# f1()和f2()的调用结果互不影响


# 闭包
# 注意到返回的函数在其定义内部引用了局部变量args，所以，当一个函数返回了一个函数后，其内部的局部变量还被新函数引用
# 另外需要注意的问题是，返回的函数并没有立即执行，而是直到调用了f()才执行
def count():
    fs = []
    for i in range(1, 4):
        def f():
            return i * i
        fs.append(f)
    return fs

f1, f2, f3 = count()
print f1(), f2(), f3()
# 结果全部都是9，原因在于返回的函数引用了变量i，但是它并非立即执行
# 等到3个函数都返回时，他们所引用的变量i已经变成了3，因此最终结果为9
# 返回闭包时，牢记的一点是，返回函数不要引用任何循环变量，或者后续会发生变化的变量
# 如果一定要引用循环变量怎么办？方法是再创建一个函数，用该函数的参数绑定循环变量当前的值，无论该循环变量后续如何更改
# 已绑定到函数参数的值不变
def count_a():
    fs = []
    for i in range(1, 4):
        def f(j):
            def g():
                return j * j
            return g
        fs.append(f(i))
    return fs

f1, f2, f3 = count_a()
print f1(), f2(), f3()

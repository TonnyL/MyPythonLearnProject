# -*- coding:utf-8 -*-

# 在python中，定义一个函数需要使用def语句，依次写出函数名、括号、参数和冒号:，然后在缩进块中编写函数体
# 函数的返回值用return语句返回
def my_abs(x):
    if x >= 0:
        return x
    else:
        return -x

print my_abs(-1)

# 如果没有return语句，函数执行完毕后也会返回结果，结果为None
# return None可以简写为return

# 空函数
# 如果要定义一个什么都不做的函数，可以直接用pass语句
def nop():
    pass

# pass语句什么都不做，那有什么用？
# 实际上pass语句可以用来做占位符，比如现在还没有想好要怎样写函数的代码，可以先用pass语句占位，让代码先跑起来

# pass还可以用于其他语句里，例如
age = 10
if age >= 18:
    pass

# 如果缺少pass，代码运行时就会出现错误

# 参数检查
# 调用函数时，如果参数个数不对，python解释器就会检查出来，并产生TypeError
# 但是如果参数类型不正确，python解释器就不能检查出来了
# 修改my_abs()的代码，对参数类型进行检查，只允许整数和浮点类型
# 数据类型检查可以通过isinstance()实现
def my_abs2(x):
    if not isinstance(x, (int, float)):
        raise TypeError('Invalid type')
    if x >= 0:
        return x
    else:
        return -x

# print my_abs2('a') TypeError('Invalid type')
print my_abs2(-1)

# 返回多个值
def multi_result(old_x, old_y):
    if not isinstance(old_x, (int, float)):
        return TypeError('Invalid type')
    elif not isinstance(old_y, (int, float)):
        return TypeError('Invalid type')
    else:
        return old_x*3.14,old_y*3.14

new_x, new_y = multi_result(2, 3)
print new_x, new_y
print multi_result(2, 3)
# 从第二次调用multi_result可以返现，返回值其实是一个tuple。
# 但是，返回一个tuple可以省略括号，而多个变量同时接收一个tuple，按位置赋值

# 小结
# 1.定义函数时，需要确定函数名和参数个数
# 2.如果有必要，先对参数做数据类型检查
# 3.函数体内部可以用return随时返回结果
# 4.函数体执行完成也没有return时，自动return None
# 5.函数可以返回多个值，但其实返回的是一个tuple
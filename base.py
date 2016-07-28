# -*- coding: UTF-8 -*-

# python基础
# python中的数据类型

# 1.整数
# python可以处理任意大小的整数，包括负整数
# 其中16进制的表示方法为 前缀(0x)+(0-9|a-f)
# 2.浮点数
# 表示方法和平时我们使用的方法相同，如果数字很大或者很小，可以用科学计数法
# 3.字符串
# 用""或者''包围的文本即字符串
# 必要的时候可以用\，进行转义
# 如果字符串中有很多字符都需要转义，可以使用 r"..."表示内部的字符串不需要转义，例如
print r"hello\n world"
# 如果字符串内部有很多换行，可以用'''...'''表示多行内容
print '''line1,
line2,
line3.\n'''

# 4.布尔值
# 一个布尔值只有True或者False两种值，需要注意大小写
result = 1>2
print result
# 布尔值可以进行与(and)、或(or)、非(not)运算
# True and True --> True
# True and False --> False
# True or False --> True
# True or True --> True
# False or False --> False
# not True --> False
# not False --> True
# 布尔值常用于if语句中
if 1>2:
    print '1 is larger than 2\n'
else:
    print '1 is less than 2\n'

# 5.空值
# 不同于java中空值用null表示，python中空值用None表示
# None不同于0，因为0是有意义的，None是一个特殊的空值
print None,'\n'

# 6.变量
# python是弱类型语言，变量可以为任意数据类型
# 变量的命名和java类似，必须为大小写英文、数字和下划线(_)的组合，并且不能以数字开头，例如
var = 1
print var
var = 'hello'
print var
var = True
print var
var = None
print var
print '\n'

# 7.常量
# 常量就是不能变的变量。在python中，通常用全部大写的变量名表示常量
PI = 3.1415926
print PI,'\n'
# 事实上，PI仍然是一个变量，python并没有任何机制保证PI不会改变
# 所以，用全部大写的变量名表示常量只是一个习惯上的用法
# 如果你一定要改变PI的值，python并不能阻止你
# 除法，取余等操作均和java中类似

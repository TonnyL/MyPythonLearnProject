# -*- coding:utf-8 -*-

# 条件判断
# python的缩进规则，如果if语句判断为True，就把缩进的语句执行了，否则什么都不做
age = 17
if age >= 18:
    print 'Adult'
else:
    print 'Teen'
# 需要注意的是，if语法和java中不同，条件语句后需要加冒号:
# 可以用elif做更加仔细的判断，elif是else if的缩写
age = 10
if age >= 18:
    print 'Adult'
elif age > 14:
    print 'Teen'
else:
    print 'Kid'

# if判断条件还可以简写，比如写
# if x:
#     print 'True'
# 只要x是非零数值，非空字符串，非空list，就判断为True，否则为false

# 循环
# python的循环有两种，一种是for...in循环，依次把list或者tuple中的元素迭代出来
tu = (1, 2, 3)
for elem in tu:
    print elem
# 计算从0到100的整数之和
sumary = 0
for e in range(0, 101, 1):
    sumary += e
print sumary

# 另外一种循环是while循环，只要条件满足，就不断循环，否则就退出循环
step = 1
while step < 5:
    print step
    step += 1

# 这个时候我们再回头看raw_input()
birthday = raw_input('input your birthday here:')
if birthday >= 2000:
    print '小鲜肉'
else:
    print '老腊肉'

# 当输入2001时，打印的仍然是老腊肉，为什么？
# 查看文档，可以发现，raw_input()函数获取到的内容是以string的形式返回的。
# raw_input([prompt]) -> string
# Read a string from standard input.  The trailing newline is stripped.
# If the user hits EOF (Unix: Ctl-D, Windows: Ctl-Z+Return), raise EOFError.
# On Unix, GNU readline is used if enabled.  The prompt string, if given,
# is printed without a trailing newline before reading.

# 找到原因后，一种解决思路是：将获取到内容强制转换为int形式，函数为int()
birthday = int(raw_input('input your birthday here:'))
if birthday >= 2000:
    print '小鲜肉'
else:
    print '老腊肉'

# 那如果输入的不是int类型，而是一个非整数型字符串呢？例如：ABC
# 就会出现类型转换错误了
#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 调试
# 程序能一次运行成功的概率很小，总是会各种各样的错误
# 有的错误很简单，看看错误信息就能解决，有的bug很复杂，我们需要知道出错时，哪些变量的值时正确的
# 哪些变量的值时错误的，因此，需要以一整套的调试程序来修复bug

# 第一种方法简单粗暴有效，就是直接print把可能出错的bug值打印出来
# def foo(s):
#     n = int(s)
#     print '>>> n = %d' % n
#     return 10 / n
#
# def main():
#     foo('0')
#
# main()
# >>> n = 0
# ZeroDivisionError: integer division or modulo by zero

# 用print最大的坏处就是将来还得删掉它，程序里到处都是print，运行结果也包含很多的垃圾信息
# 第二种方法，断言
# 凡是能print来辅助查看的地方，都可以用断言assert来替代
# def foo(s):
#     n = int(s)
#     assert n != 0, 'n is zero!'
#     return 10 / n
#
# def main():
#     foo('0')
# assert的意思是，表达式n ！= 0应该是True，否则后面的代码就出错
# 如果断言失败，assert语句本身就会抛出AssertError:
# Traceback (most recent call last):
#   ...
# AssertionError: n is zero!
# 程序中到处充斥这断言，和print相比好不到哪里去
# 不过，启动python解释器时可以用-o参数来关闭assert
# $ python -0 err.py
# Traceback (most recent call last):
#   ...
# ZeroDivisionError: integer division or modulo by zero
# 关闭后，就可把所有的assert语句当成pass语句来看了

# logging
# 把print替换成logging是第三种方式，和assert相比，logging不会抛出错误，而且可以输出到文件
import logging

s = '0'
n = int(s)
logging.info('n = %d' % n)
print 10 / n
# logging.info()就可以输出一段文本。运行，发现除了ZeroDivisionError,没有任何信息。怎么回事？
# 在import logging后添加一行配置就行了
logging.basicConfig(level=logging.INFO)

s = '0'
n = int(s)
logging.info('n = %d' % n)
print 10 / n
# 输出
# Traceback (most recent call last):
#   File "D:/PythonProjects/MyPythonLearnProject/debug.py", line 52, in <module>
#     print 10 / n
# ZeroDivisionError: integer division or modulo by zero
# 这就是logging的好处，它允许你指定记录信息的级别，有debug，info，warning，error等几个级别
# 当指定level=logging.INFO时，logging.debug就不起作用了
# 同理，指定level=WARNING时，debug和info就不起作用了
# 这样一来，就可以放心地输出不同级别的信息，也不用删除，最后统一指定输出哪个级别的信息
# logging的另一个好处就是通过简单的配置，一条语句可以同时输出到不同的地方，比如console和文件

# pdb
# 第四种方式就是启动python的调试器pdb，让程序单步运行，可以随时查看运行状态

# pdb.set_trace()
# 这个方法也是用pdb，但是不需要单步执行，只需要import pdb，然后在可能出错的地方放一个pdb.set_trace()
# 就设置了一个断点

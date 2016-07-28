# -*- coding: UTF-8 -*-

# 上面的这一行注释就是指明了编码的方式，这样就可以避免不同语言的文字冲突导致的乱码问题
# Unicode把所有的语言统一到一套字符编码里
# UTF-8即'可变长编码'的Unicode编码，这样可以防止Unicode编码大量英文时造成的空间浪费问题
# 由于python的诞生时间要早于Unicode标准的发布时间，所以最早的python只支持ASCII编码
# 普通的'python_learn'在python内部是ASCII编码的
# python提供了ord()和chr()函数，可以把字母和对应的数字进行相互的转换
tmp = chr(66)
print tmp
tmp = ord('a')
print tmp
# python后来增加了对Unicode的支持，以Unicode表示的字符串用u'...'表示
print u'人生苦短，我用python'
# 两种字符的转换方式：把u'xxx'转换为UTF-8编码的'xxx'用encode('xxx')
print u'人生苦短，我用python'.encode('utf-8')
# 我用的pycharm这里打印出来好像并没有变化。。。
# 好像要用python shell才会有这种效果
# u'中文'.encode('utf-8')
# '\xe4\xb8\xad\xe6\x96\x87'
# len()函数可以返回字符串中的字符数
print len(u'人生苦短，我用python')
# 反过来，把utf-8的编码转为Unicode字符集u'xxx'用decode('uft-8')方法
print '\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8')

# 通常还会在文件头部加上#!/usr/bin/env python表示这是一个python可执行程序，windows自动忽略这个注释

# 格式化
# 如果需要输出某种特定格式的字符串，例如，'你好，我叫xxx，来自xxx'
# 在python中，采用的格式化方法和c语言中一致，用%实现
print '你好，我叫%s，来自%s' % ('Tony','China')
# 常见的占位符有:%d-->整数 %f-->浮点数 %s-->字符串 %x-->十六进制数
# 字符串内部，有几个占位符，%后括号内就需要有几个变量或者值，而且顺序要对应
# 只有一个占位时，括号可以省略
# 如果你不确定用什么时，%s永远起作用，它会把任何数据类型转换为字符串
# %自己的转义方法为%%

# -*- coding: UTF-8 -*-

# 运行hello world
# print后接要输出的内容 可以使用单引号，也可以使用双引号，但是不能混用
print "Hello,world"
print 'Hello,world'
# 两种形式的输出语句效果是一样的

# 输出
# 在hello.py中，已经实现了输出。
# print语句后也可以跟上多个字符串，用逗号隔开，即可实现连成一串输出
print "hello",",","world"

# 细心一点可以发现，遇到逗号','会输出一个空格

# print语句也可以打印整数
print 300
print "100 + 200 =",100+200
# 对于100 + 200,python解释器计算出结果为300，整数结果接在字符串后，python解释器也把他视作字符串了

# 输入
# python提供了一个方法raw_input(),可以让用户输入字符串，并保存在变量中
# name = raw_input()
# print name
# 运行上面的代码时，没有任何的提示信息提示用户需要输入内容了
# 而raw_input()方法中可以有一个参数，这个参数的作用就是输出提示信息
tip = "Please input your name here \n"
name = raw_input(tip)
print name

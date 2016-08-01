#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
a test module
"""

__author__ = 'Tony'

import sys

# 使用模块
# python本身内置了很多模块，只要安装完毕，这些模块就可以立即使用
# 我们以内建的sys模块为例，编写一个hello的模块

def test():
    args = sys.argv
    if len(args) == 1:
        print 'HELLO WORLD'
    elif len(args) == 2:
        print 'HELLO %s!' % args[1]
    else:
        print 'TOO MANY ARGUMENTS'

if __name__ == '__main__':
    test()

# 使用sys模块的第一步，就是导入该模块
# import sys
# 导入sys模块之后，我们就有了变量sys指向该模块，利用sys这个变量，就可以访问sys模块的所有功能
# sys模块有一个argv变量，用list存储了命令行的所有参数
# argv至少有一个元素，因为第一个参数永远是.py文件的名称
# 例如：
# 运行python use_module.py获得的sys.argv就是['use_module.py']
# 运行python use_module.py Tony获得的sys.argv就是['use_module.py', 'Tony']
# 最后，注意这两行代码
# if __name__ == '__main__':
#     test()
# 当我们在命令行运行use_module模块文件时，python解释器把一个特殊变量__name__置为__main__
# 而如果在其他地方导入该use_module模块时，if判断将失败
# 因此，这种if测试可以让一个模块通过命令行测试运行时执行一些额外的代码，最常见的就是运行测试


# 别名
# 导入模块时，还可以使用别名，这样，可以在运行时根据当前环境选择最合适的模块
# 比如python标准库一般会提供StringIO和cStringIO两个库，这两个库的接口和功能是一样的
# 当时cStringIO是c写的，速度更快，所以，有可能看到这样的写法
try:
    import cStringIO as StringIO
except ImportError:  # 导入失败会捕获到ImportError
    import StringIO
# 这样就可以优先导入cStringIO，如果有些平台不提供cStringIO，还可以降级使用StringIO
# 导入cStringIO还用import...as...指定了别名StringIO,因此后续代码引用StringIO即可正常工作
# 还有类似simplejson这样的库，在python2.6之前是独立的第三方库，从2.6内置，所以，会有这样的写法
try:
    import json  # python >= 2.7
except ImportError:
    import simplejson as json  # python <= 2.6
# 由于python是动态语言，函数签名一致，接口就一样，因此，无论导入那个模块后续代码都能正常工作


# 作用域
# 在一个模块中，我们可能会定义很多函数和变量，但有的函数和变量我们希望给别人使用，有的函数和变量我们仅仅希望在模块内部使用
# 在python中，是通过前缀__来实现的
# 正常的函数和变量名是公开的，可以直接被引用
# 类似__xxx__这样的变量是特殊变量，可以直接被引用，但是有特殊用途，比如上面的__author__,__name__就是特殊变量
# __use_module__模块定义的文档注释也可以通过__doc__访问，我们自己的变量一般不要使用这种变量名
# 类似_xxx和__xxx这样的函数或者变量是非公开的，不应该被直接引用
# 之所以说，private函数和变量‘不应该’被直接引用，而不是‘不能’被直接引用，是因为python并没有一种方法可以完全限制访问private函数或变量
# 但是，从编程习惯上，不应该直接引用private函数或变量

# private函数或变量不应该被别人引用，那他们有什么用呢？
def _private_1(name):
    return 'hello, %s' % name
def _private_2(name):
    return 'hi, %s' % name
def greeting(name):
    if len(name) > 3:
        return _private_1(name)
    else:
        return _private_2(name)
# 我们在模块里公开greeting函数，而把内部逻辑用private隐藏起来了
# 这样，调用greeting函数不用关心内部的private函数细节
# 外部不需要引用的函数全部定义成private，只有外部需要引用的函数才定义为public

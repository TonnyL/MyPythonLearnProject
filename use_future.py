#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals  # line 18 used
from __future__ import division  # line 36 used

# 使用__future__

# python的每个新版本都会增加一些新的功能，或者对原来的功能做一些改动
# 有些改动是不兼容旧版本的，也即是在当前版本运行正常的代码，到下一个版本就可能不正常了
# 从python2.7到python3.x就有一些不兼容的改动，比如2.x里的字符串用'xxx'表示，Unicode字符串用u'xxx'表示unicode
# 而在3.x中，所有字符串都被视为unicode，因此，写'xxx'和u'xxx'是完全一致的
# 而在2.x中以'xxx'表示的str字符串就必须写成b'xxx',以此表示二进制字符串
# python提供了__future__模块，把下一个新版本的特性导入到当前版本，于是我们可以在当前版本中测试一些新版本的特性

# 为了适应python3.x新的字符串的表示方法，在2.7版本中，可以通过unicode_literals来使用python3.x的新的方法
# still running on Python 2.7

print '\'xxx \' is unicode?', isinstance('xxx', unicode)
print 'u\'xxx\' is unicode?', isinstance(u'xxx', unicode)
print '\'xxx\' is str?', isinstance('xxx', str)
print 'b\'xxx\' is str?', isinstance(b'xxx', str)
# 'xxx ' is unicode? True
# u'xxx' is unicode? True
# 'xxx' is str? False
# b'xxx' is str? True

# 注意到上面的代码仍然在Python 2.7下运行，但结果显示去掉前缀u的'a string'仍是一个unicode，而加上前缀b的b'a string'才变成了str：

# 类似的情况还有除法运算，在python2.7中，对于除法运算有两种情况，如果是整数相除，结果仍是整数，余数会被扔掉，这种除法叫做‘地板除’
print 10 / 3
# 要做到精确除法，必须把其中一个数变成浮点数
print 10.0 / 3
# 而在python3.x中，所有的除法都是精确除法，地板除用//表示
# 如果想在python2.7的代码中直接使用python3.x的除法，可以通过__future__的division实现
print 10 / 3
print 10.0 / 3
print 10 // 3

# 3.33333333333
# 3.33333333333
# 3

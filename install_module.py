#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
A introduction to how to install python module
"""

# 在python中，安装第三方模块，是通过setuptools这个工具完成的
# python有两个封装了setuptools的包管理工具：easy-install和pip，目前官方推荐使用pip
# 如果使用Mac或者Linux，安装pip这个步骤可以跳过
# windows下，在命令行提示符窗口下尝试运行pip，可以看到相关的信息
# 如果在首次安装时没有勾选pip，可以到https://pip.pypa.io/en/latest/installing/，按照步骤安装即可
# 然后就可以安装第三方库了

# 例如安装httpie
# 运行命令pip install httpie
# 安装完成后就可以使用了
# 其他一些第三方的库还有MySQL的驱动，MySQL-Python，用于科学计算的库numpy，用于生成文本的模板工具Jinja2等等


# 模块搜索路径
# 当我们试图加载一个模块时，python会在指定路径下搜索对应的py文件，如果找不到，就会报错
# >>> import mymodule
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# ImportError: No module named mymodule
# 默认情况下，python解释器会搜索当前目录，所有已安装的内置模块和第三方模块，搜索路径存放在sys模块的path变量中
# >>> import sys
# >>> sys.path
# ['', '/Library/Python/2.7/site-packages/pycrypto-2.6.1-py2.7-macosx-10.9-intel.egg', '/Library/Python/2.7/site-packages/PIL-1.1.7-py2.7-macosx-10.9-intel.egg', ...]
# 如果我们要添加自己的搜索目录，有两种方法
# 1. 直接修改sys.path，添加要搜索的目录
# >>> import sys
# >>> sys.path.append('/Users/michael/my_py_scripts')
# 这种方式在运行时修改，运行结束后失效
# 2. 设置环境变量PYTHONPATH,该环境变量的内容会被自动添加到模块搜索路径当中
# 设置方式和设置Path环境变量相似
# 只需要添加自己的搜索路径，python本身的搜索路径不受影响
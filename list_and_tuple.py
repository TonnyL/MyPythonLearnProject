# -*- coding:utf-8 -*-

# list
# python内置的一种数据类型。list是一种有序的集合，可以随时添加和删除其中的元素。
chars = ['a','b','c']
print chars
# 获取list的长度
print len(chars)
# list可以用索引访问单个元素，索引从0开始
print chars[0]
print chars[1]
print chars[2]
# 如果索引越界，就会产生一个IndexError，所以确保索引不要越界
# 获取最后一个元素，除了计算所以位置之外，还可以使用索引-1，直接获取
print chars[-1]
print chars[-2]
# 倒数获取元素时也是有可能产生数组越界错误的

# 数组的长度是可变的，可以通过append()方法添加元素
chars.append(1)
print chars
# 这里可以看到，list中的元素可以是不同类型的

# 也可以插入元素到指定位置
chars.insert(0, 'a')
print chars
# 要删除末尾的元素时，可以通过pop()方法
chars.pop()
print chars

print chars.pop(-1)
# 可以看到，如果直接打印执行pop()函数的结果，那么获取的就是pop()出的这个元素
# pop(i)函数中，i的值即索引

# 如果要替换某个位置的元素，可以直接赋值到这个元素
chars[1] = 'replaced'
print chars

# list中的元素也可以是另外一个list
another_list = ['A', 'B', 'C']
chars.append(another_list)

print chars

# 如何获取元素'A'呢？可以通过二维数组的形式
print chars[3][0]

# 如果一个list中没有元素，也就是一个空的list，那么他的长度为0
print len([])


# tuple
# tuple也是一种有序列表，tuple和list非常类似，但是tuple一旦初始化就不能更改
tu = ('t1', 2, True)
print tu
# 现在这个tuple的值就不能再改变了，他没有append(),没有insert()这样的方法
# 获取元素的方法和list相同，也是通过索引进行访问，但是不能赋值为另外的元素

# 不可变的tuple相对于list有什么意义呢？因为tuple是不可变的，所以代码更安全，能够使用tuple的尽量使用tuple代替list

# 但是tuple也是存在陷阱的，当你定义一个tuple时，元素必须确定下来，例如上面的tu
# 如果要定义一个空的tuple，可以写成
t = ()
print t
# 但是要定义一个只有一个元素的tuple，如果这样定义
tuple_only_one_element_w = (1)
print tuple_only_one_element_w
# 定义的并不是tuple，而是1这个数，这是因为()括号既可以表示tuple，又可以表示数学公式中的小括号，这里就产生了歧义
# 因此python规定，只有一个元素的tuple定义时必须加上逗号,消除歧义
tuple_only_one_element_r = (1,)
print tuple_only_one_element_r

# ‘可变’的tuple
changeable_tuple = (1, 2, ['c1', 'c2'])
print changeable_tuple
changeable_tuple[2][0] = 'c3'
print changeable_tuple
# 表面上tuple的元素确实变化了，但其实变化的并不是tuple的元素，而是list的元素。
# tuple一开始指向的list并没有改成别的list，所以tuple所谓的'不变'是说，tuple的每个元素，指向永远不变
# 即指向'a',就不能改为指向'b',指向一个list，就不能指向其他对象，但是这个对象list本身是可变的
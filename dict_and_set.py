# -*- coding:utf-8 -*-

# dict(dictionary,即字典)
# dict是一种使用键值对(key-value)存储的形式，具有极高的查找速度
# eg:
hometown = {'Allen': 'LA', 'Bob': 'Washington', 'Chris': 'San Francisco'}
print hometown['Allen']
# 为什么dict的查询速度非常快呢？因为dict的原理和查字典是一样的。给定一个key，dict内部就可以直接计算出key对应的value的存放地址
# 直接就可以取出来，所以速度非常快
# 把数据放入dict的方式，除了初始化指定时，还可以通过key放入
hometown['David'] = 'Toronto'
print hometown['David']
print hometown
# 由于key-value对应的唯一性，如果一个key存放多个value，后面的值就会覆盖前面的值
hometown['David'] = 'Miami'
print hometown['David']
# 如果key不存在，就会报错
# print hometown['Frank'] KeyError: 'Frank'
# 要避免key不存在的错误，有两种办法，一是通过in判断key是否存在
print 'Frank' in hometown
# 二是通过dict提供的get方法，如果key不存在，可以返回None，或者自己指定
print hometown.get('Frank', 'Phoenix')
print hometown.get('Eric')
# 需要注意的是，dict内部存放的顺序和key放入的顺序是没有关系的

# 和list比较，dict有以下的特点：
# 1. 查找和插入的速度非常快，不会随着key的增加而增加
# 2. 需要占用大量的内存，内存浪费多
# 而list和dict相反：
# 1. 查找和插入的速度随着元素的增加而增加
# 2. 占用空间少，内存浪费少
# 所以，dict是一种用空间换取时间的方法
# dict可以用在需要高速查找的很多地方，在python代码中几乎无处不在，特别需要记住的一点，dict的key必须是不可变对象
# 这是因为dict根据key来计算value的位置，如果每次计算key得到的结果不同，那么dict内部就混乱了
# 通过计算key值得到value位置的算法称作Hash(哈希)算法
# 要保证hash值不变，那么作为key的对象就不能变
# 在python中，字符串、数值等都是不可变的，因此都可以作为key，但是list是可变的，所以list不能作为key
number_dict = {1: 'No.1', 2: 'No.2', 3: 'No.3'}
print number_dict[1]

# set
# set和dict类似，也是一组key的组合，但是不存储value，所以在set中，没有重复的key
# 要创建一个set，需要提供list作为输入集合
list_ex = [1, 2, 3]
set1 = set(list_ex)
print set1
# 注意，传入的参数list_ex是一个list，而显示的set1([1, 2, 3])只是告诉你这个set内部有1，2，3这三个元素，显示的[]不表示这是一个list
# 重复的元素在set中被自动过滤
list_ex2 = [1, 4, 5]
set1 = set(list_ex2)
print set1
# 通过add(key)方法可以添加元素到set中，可以重复添加，但是不会有效果
set1.add(6)
for i in [2, 3, 9, 0]:
    set1.add(i)
print set1
# 通过remove(key)方法可以删除元素
set1.remove(1)
# set1.remove(8) 移除一个并不存在的元素时，也会报错key error
# set可以数学意义上的无序和无重复元素的集合，因此，两个set可以做数学意义上的交和并等操作
# set和dict的唯一区别就是没有存放对应的value，但是set和dict的原理一样，同样不可以放入可变对象
# 因为无法判断两个可变对象是否相等，也就无法保证set内部‘不会有重复元素’

# 再议不可变对象
# 对于可变对象，例如list，对list进行操作，list内部的内容会变化，例如
a = ['a', 'c', 'b']
a.sort()
print a
# 而对于不可变对象，例如string
a = 'abc'
a.replace('a', 'A')
print a
# 虽然string有一个replace()方法，但是输出结果可以看出来，a的值并没有发生变化，为什么？
# 先看下面的代码
print 'abc'.replace('a', 'A')
# 这里有发生了变化，和上面不同，为什么？
# 这是因为：a是变量，而字符串'abc'才是字符串对象！

# tuple虽然是不变对象，但是把tuple放入dict或者set中，为什么不行呢？
# t = (1, 2, [1, 3])
# print set(t)
# TypeError: unhashable type: 'list'
# 虽然tuple本身不变，但是其中的list是可变的，这也就意味着不能计算list的hash值，当然也就不能加入到set中了

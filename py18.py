# 可迭代对象Iterable和迭代器Iterator

#str,list,tuple,set,dict都是可迭代对象，但不是迭代器。
#可迭代对象：可以被for循环遍历的对象，即实现了__iter__()方法。
#迭代器：可以被next()函数调用并不断返回下一个值的对象，即实现了__next__()方法。

# for循环工作原理：
# 1、首先，for循环会调用可迭代对象的__iter__()方法，获得一个迭代器对象。
# 2、然后，for循环会不断调用迭代器的__next__()方法，获得下一个值，并将其赋值给循环变量。
# 3、如果迭代器的__next__()方法没有返回值（即已经到达可迭代对象的末尾），则for循环会自动退出。
# isinstance()函数可以判断一个对象是否是可迭代对象。或者已知类型

from collections.abc import Iterable, Iterator
str_obj = "hello world"
print(isinstance(str_obj, str))# True




# 迭代器Iterator
# 迭代器是可以被next()函数调用并不断返回下一个值的对象。
# 迭代器对象必须实现__iter__()和__next__()方法。
# iter()获取可迭代对象的迭代器
# next()获取迭代器的下一个值



#可迭代对象Iterable和迭代器Iterator的区别：
# 可迭代对象：可以被for循环遍历的对象，即实现了__iter__()方法。
# 迭代器：可以被next()函数调用并不断返回下一个值的对象，即实现了__next__()方法。

#可迭代对象不一定是迭代器，但迭代器一定是可迭代对象。




# 自定义迭代器类


class MyIterator:
    def __init__(self, start, end):
        self.start = start
        self.end = end



    def __iter__(self):
        return self

    def __next__(self):
        if self.start <= self.end:
            value = self.start
            self.start += 1
            return value
        else:
            raise StopIteration()


my_iter = MyIterator(0, 5)
for i in my_iter:
    print(i)




# 生成器Generator
# 生成器是一种特殊的迭代器，它不存储所有值，而是生成值并在需要时返回。
# 生成器函数使用yield语句来返回值，而不是直接返回值。

arr=[i for i in range(10) if i%2==0]
arr_gen=(i for i in range(10) if i%2==0)
print(arr_gen)
for i in arr_gen:
    print(i)


# 生成器函数
# yield语句的作用：
# 1、类似于return语句，但是会返回一个值，并暂停函数的执行。

def my_gen(n):
    li =[]
    for i in range(n):
        li.append(i)
        yield i
        i+=1



my_gen_obj = my_gen(10)
for i in my_gen_obj:
    print(i)

#可迭代对象，迭代器，生成器之间的关系
# 可迭代对象Iterable：实现了__iter__()方法，返回一个迭代器对象。
# 迭代器Iterator：实现了__iter__()和__next__()方法，可以被next()函数调用并不断返回下一个值的对象。
# 生成器Generator：使用yield语句返回值，而不是直接返回值。
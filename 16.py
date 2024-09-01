# class Person:
#     name ="小明"
#
#     def __init__(self,age=20):
#         self.age =age #类属性：对象私有
#
#     def play(self):
#         # 在实例方法中访问类属性
#         print(f"{Person.name}正在玩耍")
#
#         print(f"他的年龄是{self.age}")
#
#     @staticmethod #静态方法 类中的函数，形参没有限制
#     def introduce():
#         print(f"{Person.name}")#静态方法可以访问类属性，但是没有意义，不能访问实例属性,静态方法与类无关
#
#     @classmethod #类方法 第一个参数是类本身，可以访问类属性和类方法
#     def say_name(cls):
#         print(f"{cls.name}说：我是{cls.__name__}")
#         #不能访问实例属性
#         print(cls)
#
#
# p = Person()
# p.age = 25
# p.play()
#  #实例属性：对象私有
# p.introduce()
# Person.say_name()



#__init__方法：实例化对象时，自动调用，用于初始化对象属性
#__new__ object基类提供的内置静态方法，1，在内存中为对象分配空间，2.返回对象的引用，3，最先被调用的方法

# class Tewster:
#     def __init__(self):
#         print("这是__init__方法")
#
#     def __new__(cls, *args, **kwargs):
#         print("这是__new__方法")
#         #对父类方法进行扩展
#         obj = super().__new__(cls) #obj是实例化的对象的引用，__new__是静态方法，形参有cls，
#         return obj
    #注意：重写__new__方法时，必须调用父类的__new__方法，否则会导致父类方法失效,

# t = Tewster()
#实例化对象的过程：
#1.首先执行__new__方法，如果没有重写，则调用父类的__new__方法，返回实例化对象
#2.执行__init__方法，初始化实例化对象的属性

# class Person:
#     def __new__(cls, *args, **kwargs):
#         print((super().__new__(cls)))
#         return super().__new__(cls)
#
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#         print(f"名字：{self.name} 年龄：{self.age}")
#
#
# p = Person("小明", 20)
# print(p)




#单例模式:对象的内存地址是一样的，所以只有一个对象

#可以理解为一个特殊的类，这个类只有一个对象
#优点：节省内存，减少不必要的资源浪费
#缺点，多线程访问，会出现线程安全问题


#设计流程
#1.定义一个类属性，初始值为None，用来记录单例对象的引用
#2.重写__new__方法
#3.进行判断，如果类属性记录的对象引用为None，则创建对象并记录，否则直接返回类属性记录的对象引用
#4.返回类属性记录的对象引用


# class Singleton:
#     obj = None
#     def __new__(cls, *args, **kwargs):
#         if  not cls.obj :
#             cls.obj = super().__new__(cls)
#         return cls.obj
#
#     def __init__(self, ):
#         pass
#
#
#
# s1 = Singleton()
# s2 = Singleton()
# print(id(s1))
# print(id(s2))
# #应用场景
# #，回收站
# #播放器
# #游戏
# #

#__doc__,类的描述信息,只对多行注释生效，包含方法的描述信息

#__module__,当亲操作对象所在的模块

#__class__当前操作对象的类
#__str()__对象的描述信息，类中定义了此方法发，默认输出该方法的返回值，必须有返回值，必须为字符串类型
#__del__()方法，对象被垃圾回收时调用，释放对象占用的资源,或者结束时被调用
#__call__()方法，使一个实例对象成为一个可调用对象，可以像函数一样调用，可以重写此方法，实现类的实例对象作为函数调用

class Person:
    """
    人类
    """
    pass

print(Person.__doc__)


#递归函数
#必须有明确的结束条件，否则会陷入无限递归
#每进行更深一层递归，问题规模会变得更小
#相邻两次重复之间有紧密联系
def factorial(n):
    s=0
    for i in range(1, 101):
        s+=i
    print(s)


#递归函数
def factorial2(n):
    if n==1:
        return 1
    return n+factorial2(n-1)

print(factorial2(100))


#斐波那契数列
def fibonacci(n):
    if n==1 or n==2:
        return 1
    return fibonacci(n-1)+fibonacci(n-2)


print(fibonacci(1))





#闭包
#闭包就是一个函数，它可以访问另一个函数的变量，并且返回一个函数。
 #n内层函数使用外层函数的局部变量
 #外层函数返回内存函数的函数名


def outer():
    n=10
    def inner():
        print(n)
    return inner

# print(outer())#f返回内层函数的内存地址
outer()()#调用内层函数

ot = outer()
ot()#调用内层函数



def outer2(m):
    n = 10
    def inner2():
        print(m+n)
    return inner2

ot2 = outer2(5)
ot2()#调用内层函数


# def test1(): #test1只不过也是个函数名，存了这个函数的引用
#     print("test1")
#
# test1() #调用test1函数
# print(test1) #打印test1函数的内存地址


#2.3 每一次开启内函数都在使用同一份闭包变量

def outer3(m):
    def inner3(n):

        print("M+N",m+n)
        return m+n

    return inner3
print(outer3(5)(30))
# print(ot3(30))#调用内层函数，并传入参数


#使用闭包的过程中，一旦外函数被调用一次，返回了内部函数的引用，虽然每次调用内函数，会开启一个函数，执行后消亡
#但是闭包变量只用一份，每次开启内函数都在使用同一份闭包变量




#装饰器
#装饰器就是一个函数，它可以修改另一个函数的行为，但又不改变原函数的定义。
#装饰器的语法：


# def decorator(func):
#     def wrapper(*args, **kwargs):
#         print("Before function call")
#         result = func(*args, **kwargs)
#         print("After function call")
#         return result
#     return wrapper

def send():
    print("send email")

def outer4(func):
    def inner():
        print("登录")

        func()
    return inner

print(outer4(send)())

#多个装饰过程，是由内到外的顺序执行的。


# 隐藏属性可以通过_类名__属性名在外部修改，但不建议这么做。
#继承，子类默认继承父类的属性和方法，可以重写父类的方法，也可以添加新的方法。mro算法
#多态，父类引用子类对象，调用父类的方法，实际调用的是子类的方法。
#super()在python中是一个特殊的类，super（）是使用super类创建出来的对象，它可以调用父类的方法。


#新式类写法：继承了object或者该类的子类
#object --对象，为所有对象提供的基类，提供了内置了一些属性和方法，


#派生类
# class Animal:
#     def walk(self):
#         print("Animal is walking")
#
# class Dog(Animal):
#     name ="富贵"
#     def bark(self):
#         print("我会咬人")


# 静态方法
# 静态方法就是不需要实例化就可以调用的方法，不需要self参数，可以直接通过类名调用。与类无关 @staticmethod装饰




 # 类方法
 # 类方法就是可以被类调用的方法，需要用@classmethod装饰器修饰，第一个参数必须是cls。
 # 类方法只能访问类属性，不能访问实例属性。

 
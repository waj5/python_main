# #线程之间共享全局变量
# import time
# from threading import Thread
#
# # li=[]
# # #写入数据
# # def write_data():
# #     for i in range(5):
# #
# #         li.append(i)
# #         time.sleep(1)
# #     print("写入数据",li)
# #
# # #读取数据
# # def read_data():
# #     print("开始读取数据",li)
# #
# #
# # if __name__ == '__main__':
# #
# #     t1 = Thread(target=write_data)
# #     t2 = Thread(target=read_data)
# #
# #     t1.start()
# #     t1.join()#阻塞线程
# #     t2.start()
# #     t2.join()#阻塞线程
#
#
# #资源竞争
# # a = 0
# # b=1000000
# # #循环一次就给a加1
# # def add_a():
# #
# #     for i in range(b):
# #         global a
# #         a += 1
# #
# #     print("a的值为",a)
# #
# #
# # # add_a()
# #
# # def add_b():
# #
# #     for i in range(b):
# #         global a
# #         a += 1
# #
# #     print("第二次a的值为", a)
# #
# # if __name__ == '__main__':
# #
# #     t1 = Thread(target=add_a)
# #     t2 = Thread(target=add_b)
# #
# #     t1.start()
# #
# #     t2.start()
#
#
# #线程同步
# #线程阻塞
# # a = 0
# # b=1000000
# # #循环一次就给a加1
# # def add_a():
# #
# #     for i in range(b):
# #         global a
# #         a += 1
# #
# #     print("a的值为",a)
# #
# #
# # # add_a()
# #
# # def add_b():
# #
# #     for i in range(b):
# #         global a
# #         a += 1
# #
# #     print("第二次a的值为", a)
# #
# # if __name__ == '__main__':
# #
# #     t1 = Thread(target=add_a)
# #     t2 = Thread(target=add_b)
# #
# #     t1.start()
# #     t1.join()#阻塞线程
# #
# #     t2.start()
# #互斥锁
# from threading import Thread, Lock
#
# lock = Lock()
# a = 0
# b=1000000
# #循环一次就给a加1
# def add_a():
#     lock.acquire()
#     for i in range(b):
#         global a
#         a += 1
#
#     print("a的值为",a)
#     lock.release()
#
# # add_a()
#
# def add_b():
#     lock.acquire()
#     for i in range(b):
#         global a
#         a += 1
#
#     print("第二次a的值为", a)
#     lock.release()
#
# if __name__ == '__main__':
#
#     t1 = Thread(target=add_a)
#     t2 = Thread(target=add_b)
#
#     t1.start()
#
#     t2.start()



#进程
#程序跑起来就是进程
#进程的状态


from multiprocessing import Process,Lock
import os


# def sing():
#     print("主进程",os.getppid())#父进程id就是这个py文件所在的进程id
#     print("唱歌")
#
# def dance():
#     print("主进程", os.getppid())
#     print("跳舞")
#
#
#
#
# if __name__ == '__main__':
#     p1 = Process(target=sing)
#     p2 = Process(target=dance)
#
#     p1.start()
#     p2.start()
#     print(p1.name)
#     print(p2.name)
#     print(p1.pid)
#     print(p1.__dir__())
#     print("主进程的父进程id：",os.getppid())



# def eat(food):
#     print("吃",food)
#
# def sleep(time):
#     print("睡",time)
#
# if __name__ == '__main__':
#     p1 = Process(target=eat,args=("苹果",))
#     p2 = Process(target=sleep,args=(10,))
#
#     p1.start()
#     p2.start()
#     p1.join()
#     p2.join()
#     print(p1.is_alive())



#进程间不共享全局变量
#为什么要有if __name__ == '__main__':
#因为如果不加这个判断，那么这个模块被导入时，就会执行里面的代码，这时就会创建两个进程，这两个进程会共享全局变量，导致数据混乱。
#2.防止Windows递归创建进程
#在Windows系统下，如果不加if __name__ == '__main__'判断，会导致递归创建进程，最终导致系统崩溃





from queue import Queue
#进程间通信
#1.Queue

#初始化一个队列
q = Queue(3)
q.put("爱你到老")
q.put("你在做梦")
q.put("年轻人不讲武德")
print(q.qsize())
print(q.empty())
print(q.get())
print(q.get())
print(q.get())
print(q.full())
q.put("我要回家")
print(q.empty())
print(q.get())

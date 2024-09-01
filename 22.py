# import time
# def task1():
#     while True:
#
#         yield "哈哈哈"
#         time.sleep(1)
#
# def   task2():
#     while True:
#         yield "嘿嘿"
#         time.sleep(1)
#
#
#
# if __name__ == "__main__":
#     t1=task1()
#     t2=task2()
#     # print(t1)
#     # print(next(t2))
#     # print(next(t1))
#
#     while True:
#         print(next(t2))
#         print(next(t1))
# from greenlet import greenlet
#
#
# def sing():
#     print("在唱歌")
#     g2.switch()
#     print("唱完了")
#
#
# def dance():
#     print("在跳舞")
#     print("跳完了")
#     g1.switch()
#
#
# if __name__ == "__main__":
#     g1 = greenlet(sing)
#     g2 = greenlet(dance)
#     g1.switch()
#     g2.switch()


import gevent

# gevent.spawn() # 创建一个协程:参数是函数
# gevent.join() # 等待协程结束
# gevent.sleep() # 让出控制权
# gevent.kill() # 杀死协程
# gevent.joinall() # 等待所有协程结束:参数是携程列表
#

# def sing():
#     print("在唱歌")
#     gevent.sleep(2)
#     print("唱完了")
#
#
# def dance():
#     print("在跳舞")
#     gevent.sleep(1)
#     print("跳完了")
#
#
#
# if __name__ == "__main__":
#     g1 = gevent.spawn(sing)
#     g2 = gevent.spawn(dance)
#     g1.join()
#     g2.join()
#


# def sing(name):
#     gevent.sleep(1)
#     for i in range(3):
#         print(f"{name}在唱歌{i+1}此")
#     # print(f"唱歌的小孩是{name}" )
#
#
# def dance(name):
#     gevent.sleep(2)
#     print(f"跳舞的小孩是{name}")
#
#
# if __name__ == "__main__":
#     gevent.joinall(
#         [
#             gevent.spawn(sing, "小明"),
#             gevent.spawn(sing, "小张"),
#             gevent.spawn(dance, "小红"),
#         ]
#     )


# monkey补丁

# from gevent import monkey; monkey.patch_all()
# import time
# def sing(name):
#     time.sleep(1)
#     for i in range(3):
#         print(f"{name}在唱歌{i+1}此")
#     # print(f"唱歌的小孩是{name}" )
#
#
# def dance(name):
#     time.sleep(2)
#     print(f"跳舞的小孩是{name}")
#
#
# if __name__ == "__main__":
#     gevent.joinall(
#         [
#             gevent.spawn(sing, "小明"),
#             gevent.spawn(sing, "小张"),
#             gevent.spawn(dance, "小红"),
#         ]
#     )
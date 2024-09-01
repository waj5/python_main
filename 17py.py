# tell()显示文件当前位置，
# seek(offset, whence=0)移动指针到指定位置
# offset: 偏移量，表示移动的字节数
# whence: 起始位置，0代表从文件开头，1代表当前位置，2代表文件末尾

"""
1.文件重命名：os.rename(I旧文件名，新文件名)
2.删除文件：os.remove(目标文件名)
3.创建文件夹：os.mkdir(文件夹名)
4.获取当前目录：os.getcwd()
5.获取目录列表：os.listdir(目录)
6.删除文件夹：os.rmdir(文件夹名)
"""
import os
print(os.listdir())
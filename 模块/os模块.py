# os模块
import os
print(os.getcwd()) # 获取当前工作目录：/Users/sivan/PycharmProjects/python_study/模块
# os.chdir('../')  # 改变当前工作目录
# print(os.getcwd())
# print(os.curdir) # 获取当前目录：.
# print(os.pardir) # 获取上级目录：..
# os.makedirs('/Users/sivan/day2/abc/def') # 创建多层递归目录
# os.removedirs('/Users/sivan/day2/abc/def') # 若目录为空，则删除，并递归到上一级目录，若也为空，则删除上级目录
# os.mkdir('./test')  # 生成单级目录
# os.mkdir('./test/text')
# os.rmdir('./test/text') # 删除单级目录，若目录为空则删除 若目录不为空则无法删除
print(os.listdir('../'))
# os.remove('test/text/1') # 删除文件
# os.rename('test/1/1','test/1/2') # 重命名文件或目录
#
# print(os.stat('./'))
# info = os.stat('./')
# print(info.st_size)  # 文件大小

print(os.sep)   # 获取当前系统的文件分隔符，Windows下是\\，Linux下/
print(os.linesep) # 换行符 Windows：\r\n，linux：\n，mac：\r
print(os.pathsep)  #
print(os.system('ls'))
print(os.environ)
print(os.path.abspath('./'))  # 获取绝对路径
print(os.path.split('./test/1/2'))  # 目录分割：根据最后一个斜杠进行分割：('./test/1', '2')

print(os.path.dirname('test/1'))  # 获取最后一个文件的上一级目录名：test
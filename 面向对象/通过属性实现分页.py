# class Pagination():
#     def __init__(self,current_page):
#         try:
#             p = int(current_page)
#         except Exception as e:
#             p = 1
#         self.page = p
#
#     @ property
#     def start(self):
#         return (self.page-1)*10
#
#     @ property
#     def end(self):
#         return self.page*10
#
# list = []
# for i in range(100):
#     list.append(i)
# while True:
#     current_page = input('请输入要查看的页码')
#     if current_page == 'q':
#         break
#     obj = Pagination(current_page)
#     print(list[obj.start:obj.end])


class A:
    def f1(self):
        print('get')
        return 'f1'
    def f2(self,var):
        print(var)
        return var
    def f3(self):
        print('del')
        return 'f3'

    per = property(fget=f1,fset=f2,fdel=f3)

a = A()
a.per   # 执行f1
a.per = 111  # 执行f2
del a.per    # 执行f3

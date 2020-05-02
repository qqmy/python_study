# 偏函数 通过functools模块被用户调用
'''
函数在执行时，要带上所有必要的参数进行调用，但是，有时参数可以在函数被调用之前提前获知，在这种情况下，一个函数有一个或者
多个参数预先就能用上，以便函数能用更少的参数进行调用
偏函数是将所要承载的函数作为partial()函数的第一个参数，原函数的各个参数一次作为partial()函数的后续参数，除非使用关键字参数

原函数fun(x,y)
偏函数partial(fun,n)
fun1=partial(fun,n)
fun(x,y)等价于fun(n,x)

'''
# eg
from functools import partial

# # 原函数
# def mod(x,y):
#     return x%y
#
# mod1 = partial(mod,100)  # 原函数mod作为partial()函数的第一个参数，100作为partial()函数的第二个参数
# print(mod1(1)) # 实际上等价于mod(100,1)
# # 使用关键字参数
# mod2 = partial(mod,y=100)
# print(mod2(1)) # 等价与moda(1,100)

# eg2 简单GUI
import tkinter
root = tkinter.Tk()
myButton = partial(tkinter.Button, root,fg ='white',bg='blue')
b1 = myButton(text='Button 1')
b2 = myButton(text='Button 2')
qb = myButton(text='QUIT',bg='red',command=root.quit)
b1.pack(fill = tkinter.X,expand = True)
root.title('PEAs！')
root.mainloop()


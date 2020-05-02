def fun():
    print('hello')
    # return 1  # 结束函数，并返回一个对象
    # return 1,2,[23,4] # 如果返回对个对象，解释器会将其封装成一个元组(1,2,[23,4])
    # print(1)  # 不会执行
    # 如果不写return python默认会return一个None

print(fun())


# a = [1,2,3,4,5,[10,89]]
# a2 = a[:]  # 相当于a.copy()完成一个浅拷贝
# a2 = a.copy()
# a3 = a        # 拷贝文件，文件可变时互相影响，不可变时不会互相影响
# b = {1:2}
# b1 = b
# b1[1] = 'ss'
# print(b)
# print(b1)
# a3[0] = 3
# a2[0] = 2
# a[0] = 4
# print(a)
# print(a2)
# print(a3)


# a = [1,(),{1:'ss'}]
# b = a
# a[2] = 2
# print(a,b)

# a = [[1,2],3,4]
# b = a.copy()
# a[1] = 0
# print(a,b)

'''
a = int/str
b = a b指向a指向的内存空间
若此时修改a或者b则会对其重新开辟一个内存空间，不会影响另外一个值
eg：
a = 1
b = a
a = 2
print(a,b)  结果：2，1

a = []/{}
b = a b指向a指向的内存空间
若此时修改a或者b中元素的值，不会重新开辟新的内存空间，所以会互相影响
eg：
a = [1,2,3]
b = a
b[0] = 0
print(a,b)  结果：[0, 2, 3] [0, 2, 3]

浅拷贝
浅拷贝只拷贝一层，修改第一层数据时互不影响，第二层里面的数据是共享的，若修改则会互相影响
eg：
a = [[1,2],3,4]
b = a.copy()
a[1] = 0
print(a,b)  结果：[[1, 2], 0, 4] [[1, 2], 3, 4]
a[0][0] = 0
print(a,b)  结果：[[0, 2], 0, 4] [[0, 2], 3, 4]

深拷贝
copy.deepcopy(husband)
原数据和拷贝后的数据互不影响
import copy
husband = ['小辉',123,[15000,9000]]
wife = copy.copy(husband)  # shallow copy浅拷贝
wife[0] = 'xiaopang'
wife[1] = 345

xiaosan = copy.deepcopy(husband) # deep copy深拷贝
xiaosan[0] = 'jinxin'
xiaosan[1] = 666

xiaosan[2][1] -= 1999
husband[2][1] -= 3000
print(husband)
print(wife)
print(xiaosan)
'''
import copy
husband = ['小辉',123,[15000,9000]]
wife = copy.copy(husband)  # shallow copy浅拷贝
wife[0] = 'xiaopang'
wife[1] = 345

xiaosan = copy.deepcopy(husband) # deep copy深拷贝
xiaosan[0] = 'jinxin'
xiaosan[1] = 666

xiaosan[2][1] -= 1999
husband[2][1] -= 3000
print(husband)
print(wife)
print(xiaosan)
# 集合的创建(无序，不重复）
# s = set('hello')
# print(s)  # {'e', 'o', 'h', 'l'}  # 集合元素不能重复，且无顺序，不能通过索引来查找,或者切片操作
# s1 = ['alvin','hello','alvin']
# s2 = set(s1)
# s3 = list(s2)
# print(s2)
# print(s3)

# li = [1,[2,3],4]
# s = set(li)  # unhashable type: 'list' 集合的元素必须是可哈希的，既不可变

# li = [2,3,'alex']
# s = set(li)
# print(2 in s) # True 判断元素是否在集合里
# s.add('hello')  # 添加一个元素
# s.update('hello')  # 参数为可迭代对象，添加多个元素，结果：{2, 3, 'e', 'alex', 'o', 'h', 'l'}
# s.update([1,'s'])  # {1, 2, 3, 'alex', 's'}
# s.remove(1)  # 删除元素
# s.pop()   # 删除，随机删除
# s.clear()  # 清空
# print(s)

# del s
# print(s) # 报错

a = set([1,2,3,4,5,6])
b = set([5,6,7,8,9,10])
# 集合等价
print(set('alex') == set('alexxxx'))  # True
# 子集
print(a.issubset(b))     # a是b的子集 False
print(set('alex') < set('alexcsa'))  # True 前面的集合是后面的子集
# 父集 超集
print(a.issuperset(b))   # a是b的父集 false
print(set('alex') > set('alexcsa'))  # False
print()
print(set('alex') == set('alex'))  # False
# 交集，并集，差集

print(a.intersection(b))  # 交集{5, 6}
print(a & b)
print(a.union(b))         # 并集{1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
print(a | b)
print(a.difference(b))    # 差集{1, 2, 3, 4} in a not in b
print(a - b)
print(a.symmetric_difference(b)) # 对称差集 既不在a里也不在b里 {1, 2, 3, 4, 7, 8, 9, 10}
print(a ^ b)
# 集合作用：去重，关系测试：交集，并集，差集，对称差集等

'''
要求：
输入一个字符串，按字典序打印出该字符串的所有排列。
例如输入字符串abc，则打印出由字符串a，b，c所能排列出来的所有字符串abc，acb，bac，cab和cba

分析：
求整个字符串的排列，可以看出两步：
首先求所有可能出现在第一个位置的字符，既把第一个字符和后面的所有字符交换
然后固定第一个字符，求后面所有的字符的排序，此时仍把后面的字符看成两部分，第一个字符和后面的字符
然后重复上述步骤
通过递归的方式，递归去处理确定字符值后的所有字符，递归的终止条件是需要处理的字符长度为1

'''
def permutation(data):
    if len(data) <=1:
        return [data]
    list = []
    for i in range(len(data)):
        for j in permutation(data[0:i]+data[i+1:]):
            list.append(data[i]+j)
    return list

list = permutation('abc')
print(list)

a = range(10)
print(a)
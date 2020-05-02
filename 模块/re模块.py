# 正则表达式
'''
正则表达式是用来干嘛的？
匹配字符串
简介：
就其本质而言，正则表达式（或RE）是一种小型的、高度专业化的编程语言，在（python中）它内嵌在python中，并通过re模块实现
正则表达式模式被编译成一系列的字节码，然后由用C编写的匹配引擎执行
'''
# s = 'hello world'
# print(s.find('l'))   # 查找元素，返回他第一个匹配的索引 如果没有则返回-1
# ret = s.replace('ll','xx')
# print(ret)
# print(s.split('w'))

# string提供的方法是完全匹配
# 引入正则：模糊匹配

import re

# findall(pattern, string, flags=0) pattern：规则，string：要匹配的字符串 flags修改匹配规则，可以让.匹配任意字符包括换行符
# re.findall('w\w{2}l','hello world')  # 全部找到，返回一个数组
# print(re.findall('w..l','hello world'))   #'worl']
# print(re.findall('w..l','hello w\nld'))  # .代指任意一个字符，不包括换行符（\n）  结果：[]
#
# print(re.findall('^h...o','hjasdfhello'))   # [] ^代表只从起始位置开始匹配
# print(re.findall('^h...o','hjasofhello'))  # ['hjaso']
#
# print(re.findall('h...o$','hjasofhello'))  # $代表只从结束位置开始匹配 ['hello']
# print(re.findall('h...o$','hjasofhelloo'))  # []

# 重复匹配[0,+oo]
# print(re.findall('ho*','hello hooo hhoo'))  # ['h', 'hooo', 'h', 'hoo']
# print(re.findall("ab*","cabb3abcbbacaa"))   # 匹配*号前的字符0次或多次 结果：['abb', 'ab', 'a', 'a', 'a']
# # 可能出现的结果有单个a，a连续单个b，a连续多个b
# print(re.findall('.*','uehalfhjefacdncehcndn  cffjja'))  # ['uehalfhjefacdncehcndn  cffjja', '']

# print(re.findall('ab+', 'hellab abb b aaa'))  # 匹配+号之前的一个字符1次或多次 结果：['ab', 'abb']
# print(re.findall('a?b', 'aaaabhghabfb'))  # 匹配前一个字符1次或0次 结果['ab', 'ab', 'b']
#
# print(re.findall('a{3}b', 'abaabaaaab aaab'))  # 匹配前一个字符m次  结果：['aaab', 'aaab']
# print(re.findall('a{1,3}b', 'aaaab'))  # 匹配前一个字符n到m次 贪婪匹配，返回最多的结果：['aaab']
# print(re.findall('a{1,}b', 'aab b abb'))  # ['aab', 'ab'] {1,}等价于{1,+oo}
# 结论：*等价于{0,+oo} +等价于{1,+oo} ?等价于{0,+oo}推荐前者

# 字符集
# print(re.findall('a[c,d]x', 'adx'))     # ['adx']
# print(re.findall('[c,d,e]x', 'adx'))  # ['dx']
# print(re.findall('[a-z]','adx'))
# # 字符集：取消元字符的特殊功能 除了(\ ^ -)
# print(re.findall('[*,a]','aa'))  # ['a', 'a']
# print(re.findall('[*,a]','*bshiahf'))  # ['*', 'a']
# print(re.findall('[a,,]','ahfu,fud'))  # ['a', ',']

# \
# 反斜杠后边跟元字符，去除特殊功能
# 反斜杠后面跟普通字符，实现特殊功能
# \d 匹配任何十进制数字 相当于[0-9]
# \D 匹配任何非数字字符：相当于[^0-9】
# \s 匹配任何空白字符：相当于[\t\n\r\f\v]
# \S 匹配任何非空白字符：相当于[^\t\n\r\f\v]
# \w 匹配任何字母数字字符：相当于[a-z A-Z 0-9]
# \W 匹配任何非字母数字字符：相当于[^a-z A-Z 0-9]
# \b 匹配一个特殊字符边界 （数字字母和标点符号以及空格等）

print(re.findall('\d{11}','12343567890023923ooosfjkdafj ijiafwejfnj')) # ['12343567890']
print(re.findall('\d{4}','8928893439880af12321'))  # ['8928', '8934', '3988', '1232']
print(re.findall('\sasd','fak asd'))  # [' asd']
print(re.findall('\wasd','fak asd'))  # []
print(re.findall('\wasd','fak basd'))  # ['basd']
print(re.findall('\w','fak ask'))  # ['f', 'a', 'k', 'a', 's', 'k']
print(re.findall(r'\bI','heool I am a LIST'))  # ['I']
print(re.findall(r'\bI','heool I,am a LIST'))  # ['I']


print(re.search('as','fjasb as').group()) # 匹配出第一个满足条件的结果 as
print(re.search('a.s','fjafsab aes').group()) # 匹配出第一个满足条件的结果 afs
# print(re.search('a\.','agj').group())  # AttributeError: 'NoneType' object has no attribute 'group'

print(re.findall('\\\\','a\c'))  # ['\\']
print(re.findall(r'\\','a\c'))   # 等价于上面
print(re.findall(r'\ba','abdsa')) #['a']


ret = re.search('(?P<id>\d{3})/(?P<name>\w{3})','wafeiw24wija892/ooo')  # 给组起名字，可以通过组名取到相应的值
print(ret.group())   # 892/ooo
print(ret.group('id'))  # 892 通过组名去拿相应的值
print(ret.group('name'))  # ooo
# ()分组
print(re.search('(as)+','sdifjdidaffdsasas as').group())  # 分组将括号里的内容作为一个整体 asas
print(re.search('(as)|3','asjwj3dsa').group())  # as

'''
'.'     默认匹配除\n之外的任意一个字符，若指定flag DOTALL,则匹配任意字符，包括换行
'^'     匹配字符开头，若指定flags MULTILINE,这种也可以匹配上(r"^a","\nabc\neee",flags=re.MULTILINE)
'$'     匹配字符结尾，或e.search("foo$","bfoo\nsdfsf",flags=re.MULTILINE).group()也可以
'*'     匹配*号前的字符0次或多次，re.findall("ab*","cabb3abcbbac")  结果为['abb', 'ab', 'a']
'+'     匹配前一个字符1次或多次，re.findall("ab+","ab+cd+abb+bba") 结果['ab', 'abb']
'?'     匹配前一个字符1次或0次
'{m}'   匹配前一个字符m次
'{n,m}' 匹配前一个字符n到m次，re.findall("ab{1,3}","abb abc abbcbbb") 结果'abb', 'ab', 'abb']
'|'     匹配|左或|右的字符，re.search("abc|ABC","ABCBabcCD").group() 结果'ABC'
'(...)' 分组匹配，re.search("(abc){2}a(123|456)c", "abcabca456c").group() 结果 abcabca456c
 
 
'\A'    只从字符开头匹配，re.search("\Aabc","alexabc") 是匹配不到的
'\Z'    匹配字符结尾，同$
'\d'    匹配数字0-9
'\D'    匹配非数字
'\w'    匹配[A-Za-z0-9]
'\W'    匹配非[A-Za-z0-9]
's'     匹配空白字符、\t、\n、\r , re.search("\s+","ab\tc1\n3").group() 结果 '\t' 
   
'''

# 正则表达式的方法
# findall():所有的结果都返回到一个列表里
# search()：如果结果为空返回None，不为空返回匹配到的第一个对象，对象可以调用group方法
# match()：只在字符串开始匹配，也返回匹配到的第一个对象，对象可以调用group方法
# split()：

print(re.match('asd','asdasd asd').group())
# print(re.match('asd','aasdasd asd').group())

print(re.split('r', 'ard'))  # ['a', 'd']
print(re.split('[j,s]','asajklsa'))  # 先按照j分，分完的结果再按照s分，结果： ['a', 'a', 'kl', 'a']
print(re.split('[j,s]','sajsa'))  # ['', 'a', '', 'a'] 第一次分完的结果为['sa','sa']，再次分割时s前有一个空格

ret = re.sub('a..x','s....b','hfjsalexxdhf')  # hfjss....bxdhf  替换
print(ret)

p = re.compile('\.com')
print(p.split('jdiwoew.comniewfaj'))   # ['jdiwoew', 'niewfaj']
print(p.findall('jdiwoew.comniewfaj'))  # ['.com']

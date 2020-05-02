# def feib(n):
#     a,b=0,1
#     if n<=1:
#         yield n
#     else:
#         for i in range(n):
#             a,b = b,a+b
#             yield b
# f = feib(4)
# for i in f:
#     print(i)
#
#
# # 判断一个数组是否是包含另外一个数组
# arry1 = [1,3,4,5,]
# arry2 = [3,4,5,4]
# s1 = set(arry1)
# s2 = set(arry2)
# print(s1>=s2)
# import requests
#
# # print(requests.get('https://bj.meituan.com/ptapi/recommends'))
# # print(requests.request('GET', 'https://bj.meituan.com/ptapi/recommends').json())
# url = "https://bj.meituan.com/ptapi/recommends"
#
# payload = {}
# headers= {}
#
# response = requests.request("GET", url, headers=headers, data = payload)
#
# print(response.text.encode('utf8'))


import requests

url = "https://bj.meituan.com/ptapi/recommends?xxx=yyy"

# payload = {}
# headers= {}
#
# response = requests.request("GET", url, headers=headers, data = payload)
#
# print(response.text.encode('utf8'))

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.63 Safari/537.36'}

print(requests.get(url,headers=headers).json())
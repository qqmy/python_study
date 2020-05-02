import time
# print(help(time))
# print(time.time())  # 1587547049.892329:时间戳
# time.sleep(3)
# print(time.process_time()) # 计算cpu执行时间
# print(time.gmtime())    # 结构化时间：结果为UTC 时间 time.struct_time(tm_year=2020, tm_mon=4, tm_mday=22, tm_hour=9, tm_min=20, tm_sec=53, tm_wday=2, tm_yday=113, tm_isdst=0)
# print(time.localtime())    # 结构化时间：结果为当前时间 time.struct_time(tm_year=2020, tm_mon=4, tm_mday=22, tm_hour=20, tm_min=29, tm_sec=1, tm_wday=2, tm_yday=113, tm_isdst=0)

local_time = time.localtime()
# print(time.strftime('%Y--%m--%d %H:%M:%S',local_time))  # 自定义时间格式，2020--04--22 17:54:09
# print(time.strptime('2020--04--22 17:54:09','%Y--%m--%d %H:%M:%S'))  # 把指定格式的时间转化为结构化时间
# time_struct = time.strptime('2020--04--22 17:54:09','%Y--%m--%d %H:%M:%S')
# print(time_struct.tm_year)
# print(time_struct.tm_mday)
# print(time_struct.tm_mon)
# print(time_struct.tm_wday)
#
# print(time.ctime())  # 获取当前时间 Wed Apr 22 18:03:21 2020
# print(time.ctime(111111111102))  # 将一个时间戳转化为Sun Dec 21 13:31:42 5490

print(time.mktime(time.localtime())) # 将结构化时间转化为时间戳

import datetime

print(datetime.datetime.now())  # 获取当前时间 2020-04-22 20:32:31.002987

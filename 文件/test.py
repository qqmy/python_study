'''
文件doom.log有多列数据，
空格隔开，统计第三列的接口，按照接口出现的次数，做倒序输出
'''


def tongji(filename,i):
    f = open(filename,'r')
    api_list = []
    for line in f:
        line_lis = line.split()
        if len(line_lis)<i:
            continue
        api_list.append(line_lis[i-1])


    api_dict = {}
    for api in api_list:
        if api in api_dict:
            api_dict[api] +=1
        else:
            api_dict[api] = 1
    # print(api_dict)

    api_list = []
    for item in api_dict:
        # temp_dict = {}
        # temp_dict[item] = api_dict[item]
        api_list.append([item, api_dict[item]])

    # print(api_list)

    length = len(api_list)
    for i in range(length):
        for j in range(i, length):
            if api_list[i][1] < api_list[j][1]:
                temp = api_list[i]
                api_list[i] = api_list[j]
                api_list[j] = temp

    print(api_list)


tongji('小重山.txt',3)






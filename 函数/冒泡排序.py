# 选择排序
def sortlist(list):
    length = len(list)
    # print(length)
    for i in range(length):
        mind_id = i
        for j in range(i,length):
            if list[mind_id] > list[j]:
                mind_id = j
                list[i],list[mind_id] = list[mind_id],list[i]
    return list


print(sortlist([1, 3, 2, 4, 5, 6, 6, 10, 23, 2,4,2]))


def bubble_sort(data:list):
    size = len(data)
    for i in range(size):
        for j in range(size-i-1):
            if data[j]>data[j+1]:
                data[j],data[j+1] =data[j+1],data[j]
    return data

print(bubble_sort([1, 3, 2, 4, 5, 6, 6, 10, 23, 2,4,2]))
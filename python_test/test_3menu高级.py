# menu = {'北京':
#             {'朝阳':{'酒仙桥':{},'望京':{}},
#              '昌平':{'天通苑':{},'立水桥':{}}},
#         '上海':
#             {'浦东':{'陆家嘴':{},'外滩':{}},
#              '闵行':{}},
#         '安徽':
#             {'合肥':{'':{}},
#               '宿州':{'灵璧':{},'固镇':{}}}}
# current_layer = menu  # 实现动态循环
# parent_list = []  # 保存所有父级，最后一个元素永远都是父亲级
#
# while True:
#     for key in current_layer:
#         print(key)
#     choice = input(">>:").strip()
#     if len(choice) == 0:
#         continue
#     if choice in current_layer:
#
#         parent_list.append(current_layer)  # 在进入下一层之前把当前级（也就是下层的父亲及）保存
#         # 下一次loop，当用户选择b时，就直接取列表的最后一个元素就可以了
#         current_layer = current_layer[choice] # 改成子层
#
#     elif choice == 'b':
#         if parent_list:
#             current_layer = parent_list.pop() # 取出列表的最后一个元素，也就是下一层的父级别
#     else:
#         print('无此项')


menu = {'北京':
            {'朝阳':{'酒仙桥':{},'望京':{}},
             '昌平':{'天通苑':{},'立水桥':{}}},
        '上海':
            {'浦东':{'陆家嘴':{},'外滩':{}},
             '闵行':{}},
        '安徽':
            {'合肥':{'':{}},
              '宿州':{'灵璧':{},'固镇':{}}}}

current_layer = menu
parent_layers = []

while True:
    for key in current_layer:
        print(key)
    choice = input(">>: ").strip()

    if len(choice) == 0:continue
    if choice in current_layer:
        parent_layers.append(current_layer)
        print(parent_layers)
        current_layer = current_layer[choice]
    elif choice == 'b':
        if len(parent_layers) >=1:
            current_layer = parent_layers.pop()
            print(current_layer)
        else:
            exit()

    else:
        print('选项不存在')

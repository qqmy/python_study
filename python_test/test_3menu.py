'''
程序：三级菜单
要求：
可以一层一层的进入到所有层
打印省、市、县三级菜单
可返回上一级
可随时退出程序
'''
menu = {'北京':
            {'朝阳':['酒仙桥','望京'],
             '昌平':['天通苑','立水桥']},
        '上海':
            {'浦东':['陆家嘴','外滩'],
             '闵行':[]},
        '安徽':
            {'合肥':[''],
              '宿州':['灵璧','固镇']}}
back_flag = False
exit_flag = False
while not back_flag and not exit_flag:

    for key in menu:
        print(key)  # 打印省份
    choice = input('>>:')
    if choice in menu:
        while not back_flag and not exit_flag: # 让程序停在第二层
            for key2 in menu[choice]:
                print(key2)
            choice2 = input('>>:')
            if choice2 in menu[choice]:
                for key3 in menu[choice][choice2]:
                    print(key3)
            elif choice2=='b':
                back_flag = True
            elif choice2 == 'q':
                exit_flag == True
        else:
            back_flag = False
    elif choice =='b':
        back_flag = True


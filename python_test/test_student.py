'''
需求：一直学生列表stu_list=['大乔'，'小乔'，'周瑜'，'诸葛亮'，'嬴政']
1、显示所有的学生
2、增加学生
3、删除学生
4、更改学生信息
5、退出程序
'''
stu_list = ['大乔','小乔','周瑜','诸葛亮','嬴政']
print('1代表显示所有的学生')
print('2代表增加学生')
print('3删除学生')
print('4更改学生信息')
print('5退出程序')
while True:
    option = int(input('\t请输入你选择的操作:'))
    if option == 1:
        for i in stu_list:
            print(i)
    elif option == 2:
        addname = input('请输入要增加的学生姓名：')
        stu_list.append(addname)
        print('学生%s增加成功'%addname)
    elif option == 3:
        deletename = input('请输入要删除的学生姓名：')
        stu_list.remove(deletename)
        print('学生%s删除成功'%deletename)
    elif option == 4:
        removename = input('请输入要修改的学生姓名：')
        re_index= stu_list.index(removename)
        newname = input('请输入新的名字：')
        stu_list[re_index] = newname
    elif option == 5:
        print('拜拜')
        break

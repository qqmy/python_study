# '''
# 员工管理系统实现
# 1、数据存储
# 2、业务实现，增删改查
# 3、数据呈现
# '''
# # 1、员工存储问题
# # 2、业务实现步骤
# # 2.1、首先显示操作菜单
# # 2.2、获得用户输入的菜单编号
# # 2.3、根据菜单编号选择不同的操作执行
# # 2.4、重复上面3个步骤
# # 存储员工信息
# employee = {}
#
#
# # 菜单功能实现
# def show_menu():
#     '显示系统菜单'
#
#     print('*' * 30)
#     print('员工管理系统 V1.0')
#     print('  1:添加员工信息')
#     print('  2:删除员工信息')
#     print('  3:修改员工信息')
#     print('  4:显示所有信息')
#     print('  5：退出员工系统')
#     print('*' * 30)
#
#
# # 新增功能实现
# # 1、获得输入的员工信息
# # 2、将员工信息依据"键：值"存储到字典中，每个字典表示一个员工的完整信息
# # 3、以员工编号为键。员工信息为值，将员工信息存储到employee字典中
# def add_new_info():
#     '添加新的员工'
#     en_number = input('请输入员工编号：')
#     en_name = input('请输入员工姓名：')
#     en_salary = input('请输入员工工资：')
#     en_gender = input('请输入员工性别：')
#     # 构建员工信息字典
#     en_infor = {'name': en_name, 'salary': en_salary, 'gender': en_gender}
#     # 以员工的编号为键，存储员工信息
#     employee[en_number] = en_infor
#
#
# # 删除功能实现
# # 1、获得要删除的员工编号
# # 2、判断员工编号是否存在，如果不存在则终止函数执行
# # 3、如果员工信息存在，则根据键删除员工信息
# def remove_info():
#     en_number = input('请输入员工编号：')
#
#     if en_number in employee.keys():
#         # 删除对应编号的员工信息
#         employee.pop(en_number)
#         print('员工编号为：%s的员工信息被删除！' % en_number)
#     else:
#         print('您输入的员工编号不存在')
#
# # 显示功能实现
# def show_all_info():
#     '打印所有员工信息'
#
#     print("*"*30)
#     for em_num,em_info in employee.items():
#         print('编号：%s\t姓名：%s\t工资：%s\t性别：%s'%(em_num,em_info['name'],em_info['salary'],em_info['gender']))
#
#
#
# # 修改功能实现
# # 1、获得要修改的员工编号
# # 2、判断员工编号是否存在，如果不存在则终止修改函数执行
# # 3、首先显示员工的对于信息，并提示用户输入修改之后的值
# # 3.1、如果直接回车、表示用户无任何输入、则表示不修改
# # 3.2、如果用户输入值，则将对应信息修改为新输入的值
# def edit_info():
#     '修改员工信息'
#     em_number = input('请输入员工编号')
#     if em_number not in employee.keys():
#         print('您输入的员工编号不存在！')
#         return
#     new_name = input('编号为%s的员工姓名为%s，你要修改为：'%(em_number,employee[em_number]['name']))
#     new_salary = input('编号为%s的员工工资为%s，你要修改为：'%(em_number,employee[em_number]['salary']))
#     new_gender = input('编号为%s的员工性别为%s，你要修改为：'%(em_number,employee[em_number]['gender']))
#     if new_name != '':
#         employee[em_number]['name'] = new_name
#     if new_salary != '':
#         employee[em_number]['salary'] = new_salary
#     if new_gender != '':
#         employee[em_number]['gender'] = new_gender
#     print('编号为%s的员工信息修改成功！'%em_number)
#
# def main():
#     while True:
#         # 1、打印菜单
#         show_menu()
#         # 2、等待用户输入
#         user_operate = input('请输入您的操作：')
#         # 3、根据用户输入的操作选择做相应的事情
#         if user_operate == '1':
#             add_new_info()
#         elif user_operate == '2':
#             remove_info()
#         elif user_operate == '3':
#             edit_info()
#         elif user_operate == '4':
#             show_all_info()
#         elif user_operate == '5':
#             print('欢迎再次使用本系统！')
#             break
#         else:
#             print('您的输入有误，请重新输入！')
# main()

# 写列表中除去包含7和能被7整除的
# 方式1 列表解析器
y = [i for i in range(100) if i!=7 and i%7 !=0]
print(y)
# 方式2 if else
l = []
for i in range(100):
    if i !=7 and i%7 !=0:
        l.append(i)
print(l)
# 方式3 filter 内置函数
print(list(filter(lambda x: "7" not in str(x) and x % 7 != 0, l)))

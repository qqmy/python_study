# 装饰器实现登录，要求程序启动时打开home，finance，book三个页面
# 选择1，进入home页，选择2，进入finance页，选择3，进入book页
# 判断各个页面，如果登录就打印当前页面，如果未登录则进入登录
# home页登录方式，为京东登录
# finance页登录方式为微信登录
# book页登录方式为京东登录
# loging_statu = False


# def open_file(filename):
#     file_name = filename+'.txt'
#     file = open(file_name, 'r')
#     # lines = file.readlines()
#     name = input('name：')
#     passwod = input('password')
#     for line in file:
#         lines = line.split(':')
#         if name == lines[0].strip() & passwod == lines[1].strip():
#             print('welcome')

loging_statu = False

def loging(aurh_type):
    def autho(page):
        def inner():
            global loging_statu
            if loging_statu == False:
                if aurh_type == 'home':
                    file = open('jingdong.txt','r')
                    # lines = file.readlines()
                    name = input('name：')
                    passwod = input('password')
                    for line in file:
                        lines = line.split(':')
                        if name == lines[0].strip() and passwod== lines[1].strip():
                            print('welcome')
                            page()
                            loging_statu = True

                elif aurh_type == 'finace':
                    file = open('weixin.txt', 'r')
                    # lines = file.readlines()
                    name = input('name：')
                    passwod = input('password')
                    for line in file:
                        lines = line.split(':')
                        if name == lines[0].strip() and passwod == lines[1].strip():
                            print('welcome')
                            page()
                            loging_statu = True

                elif aurh_type == 'boook':
                    file = open('jingdong.txt', 'r')
                    # lines = file.readlines()
                    name = input('name：')
                    passwod = input('password')
                    for line in file:
                        lines = line.split(':')
                        if name == lines[0].strip() and passwod == lines[1].strip():
                            print('welcome')
                            page()
                            loging_statu = True

                else:
                    pass
            else:
                page()


        return inner
    return autho


@ loging('home')
def home():
    print('欢迎进入home页')
@ loging('finace')
def finace():
    print('欢迎进入finace页')
@ loging('book')
def book():
    print('欢迎进入book页')

while True:
    print('home')
    print('finace')
    print('book')
    page = input('请选择要进入的页面：')
    if page=='home':
        home()
    elif page=='finace':
        finace()
    elif page == 'book':
        book()
    elif page =='q':
        break
    else:
        print('输入错误请重新输入')
        continue

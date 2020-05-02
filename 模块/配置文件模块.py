import configparser

config = configparser.ConfigParser()

# config['DEFAULT'] = {'name':'qmy','gender':'nv'}
# config['bitbucket.org'] = {}
# config['bitbucket.org']['bit']='lyx'
# config['bitbucket.org']['bucket'] = 'nan'
#
# with open('config.ini','w') as configfile:
#     config.write(configfile)

config.read('config.ini')
print(config.sections())  # 获取出了默认的其他sections
print(config.default_section) # 获取默认的sections
print(config.defaults())  # 获取DEFAULT的值 是一个有序的字典 OrderedDict([('name', 'qmy'), ('gender', 'nv')])
print(config.has_section('bitbucket.org')) # 判断是section否有'bitbucket.org'
config.set('bitbucket.org','bit','ly') # 将'bitbucket.org'的bit的值改为ly，更改后需要重新写入文件
print(config.options('bitbucket.org')) # 获取指定section的值
config.write(open('config.ini','w'))

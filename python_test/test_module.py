import sys

# print(sys.path)  # 默认的搜索路径 sys.path.append(path)可以追加指定的目录
'''
['/Users/sivan/PycharmProjects/python_study/python_test', 
'/Users/sivan/PycharmProjects/python_study', 
'/Applications/PyCharm.app/Contents/helpers/pycharm_display', 
'/Library/Frameworks/Python.framework/Versions/3.7/lib/python37.zip',
 '/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7', 
 '/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/lib-dynload', 
 '/Users/sivan/PycharmProjects/python_study/venv/lib/python3.7/site-packages', 
 '/Users/sivan/PycharmProjects/python_study/venv/lib/python3.7/site-packages/setuptools-40.8.0-py3.7.egg',
  '/Users/sivan/PycharmProjects/python_study/venv/lib/python3.7/site-packages/pip-19.0.3-py3.7.egg',
   '/Applications/PyCharm.app/Contents/helpers/pycharm_matplotlib_backend']
'''

# print(sys.modules)  # 使用模块名作为键，对应的物理地址作为值

'''
{'sys': <module 'sys' (built-in)>, 'builtins': <module 'builtins' (built-in)>, 
'_frozen_importlib': <module '_frozen_importlib' (frozen)>, '_imp': <module '_imp' (built-in)>,
 '_thread': <module '_thread' (built-in)>, '_warnings': <module '_warnings' (built-in)>, 
 '_weakref': <module '_weakref' (built-in)>, 'zipimport': <module 'zipimport' (built-in)>, '_frozen_importlib_external': <module '_frozen_importlib_external' (frozen)>, '_io': <module 'io' (built-in)>, 'marshal': <module 'marshal' (built-in)>, 'posix': <module 'posix' (built-in)>, 'encodings': <module 'encodings' from '/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/encodings/__init__.py'>, 'codecs': <module 'codecs' from '/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/codecs.py'>, '_codecs': <module '_codecs' (built-in)>, 'encodings.aliases': <module 'encodings.aliases' from '/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/encodings/aliases.py'>, 'encodings.utf_8': <module 'encodings.utf_8' from '/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/encodings/utf_8.py'>, '_signal': <module '_signal' (built-in)>, '__main__': <module '__main__' from '/Users/sivan/PycharmProjects/python_study/python_test/test_module.py'>, 'encodings.latin_1': <module 'encodings.latin_1' from '/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/encodings/latin_1.py'>, 'io': <module 'io' from '/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/io.py'>, 'abc': <module 'abc' from '/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/abc.py'>, '_abc': <module '_abc' (built-in)>, 'site': <module 'site' from '/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/site.py'>, 'os': <module 'os' from '/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/os.py'>, 'stat': <module 'stat' from '/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/stat.py'>, '_stat': <module '_stat' (built-in)>, 'posixpath': <module 'posixpath' from '/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/posixpath.py'>, 'genericpath': <module 'genericpath' from '/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/genericpath.py'>, 'os.path': <module 'posixpath' from '/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/posixpath.py'>, '_collections_abc': <module '_collections_abc' from '/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/_collections_abc.py'>, '_sitebuiltins': <module '_sitebuiltins' from '/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/_sitebuiltins.py'>, '_bootlocale': <module '_bootlocale' from '/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/_bootlocale.py'>, '_locale': <module '_locale' (built-in)>, 'encodings.cp437': <module 'encodings.cp437' from '/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/encodings/cp437.py'>, 'sitecustomize': <module 'sitecustomize' from '/Applications/PyCharm.app/Contents/helpers/pycharm_matplotlib_backend/sitecustomize.py'>}

'''


# Globals()返回调用者全局名称空间的字典
# locals()返回调用者局部名称空间的字典
# def foo():
#     print('\ncalling fool().....')
#     anString = 'bar'
#     anInt = 42
#     print("foo()'s globals: ", globals().keys())
#     print("foo()'s locals: ", locals().keys())
# print("_main_'s gloabls: ", globals().keys())
# print("_main_'s locals: ", locals().keys())
# foo()

# -*- coding: UTF-8 -*-


#
# from python_test.test_class import ClassA
# ClassA.test('self',2)
# ClassA.x = 1
# ClassA.y = 2
# print(ClassA.x+ClassA.y)
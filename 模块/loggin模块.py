import logging
#
# logging.debug('debug message')
# logging.info('info message')
# logging.warning('warung messiong')
# logging.error('erro message')
# logging.critical('critical message')
# # 日志级别CRITICAL > ERROR > WARNING > INFO > DEBUG > NOTSET
# '''
# WARNING:root:warung messiong
# ERROR:root:erro message
# CRITICAL:root:critical message
# '''
# logging.basicConfig(level=logging.DEBUG,
#                     format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
#                     datefmt='%a, %d %b %Y %H:%M:%S',
#                     filename='/tmp/test.log',
#                     filemode='w')

# 自定义日志输出方式
logger = logging.getLogger()

# 定义一个文件输出对象
fh = logging.FileHandler('logger.txt','a')

# 定义一个屏幕输出对象
sh = logging.StreamHandler()

# 定义文件输出格式
format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

fh.setFormatter(format)
sh.setFormatter(format)

logger.addHandler(fh)
logger.addHandler(sh)

logger.setLevel(logging.DEBUG)

logger.info('hello')
logger.debug('hello')
# encoding:utf-8
import logging, os

path = '/Users/lijialing/develop/pythonWorkspace/python_gentleman_crawler/logs/system.log'
#path = '//192.168.3.8/home/dev/python_gentleman_crawler/logs/system.log'

logger = logging.getLogger(path)
logger.setLevel(logging.INFO)
fmt = logging.Formatter('%(asctime)s %(levelname)s %(message)s', '%Y-%m-%d %H:%M:%S')
#设置CMD日志
sh = logging.StreamHandler()
sh.setFormatter(fmt)
#设置文件日志
fh = logging.FileHandler(path, encoding="utf8")
fh.setFormatter(fmt)
#fh.encoding = "utf8"
logger.addHandler(sh)
logger.addHandler(fh)

def debug(message):
    logger.debug(message)

def info(message):
    logger.info(message)

def warn(message):
    logger.warn(message)

def error(message):
    logger.error(message)

def critical(message):
    logger.critical(message)

def exception(message):
    logger.exception(message)


if __name__ == '__main__':
    debug('一个debug信息')
    info('一个info信息')
    warn('一个warning信息')
    error('一个error信息')
    critical('一个致命critical信息')
    try:
        raise Error("error1")
    except Exception as e:
        logger.exception(e)

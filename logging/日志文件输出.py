#!/usr/local/bin/python
# -*- coding:utf-8 -*-

import logging

# 通过下面的方式进行简单配置输出方式与日志级别
# 标准输出(屏幕)未显示任何信息，发现当前工作目录下生成了logger.log
# 因为通过level=logging.INFO设置日志级别为INFO，所以所有的日志信息均输出出来了。
logging.basicConfig(filename='logger.log', level=logging.INFO)

logging.debug('debug message')
logging.info('info message')
logging.warning('warn message')
logging.error('error message')
logging.critical('critial message')

# DEBUG: 详细信息，典型地调试问题时会感兴趣
# INFO: 证明事情按照预期工作
# WARNING: 表明发生了一些意外，或者不久的将来会发生问题（如'磁盘满了'）。软件还是正常工作
# ERROR: 由于更严重的问题，软件已不能执行一些功能了
# CIRTICAL: 严重错误，表明软件已经不能继续运行了。
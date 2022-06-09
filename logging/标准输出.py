#!/usr/local/bin/python
# -*- coding:utf-8 -*-

import logging

# 默认情况下，logging模块将日志打印到屏幕上(stdout)，日志级别为WARNING(即只有日志级别高于WARNING的日志信息才会输出)，日志格式如下图所示：
# WARNING: root : warn message
# 日志级别: Logger实例名称: 日志消息内容
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
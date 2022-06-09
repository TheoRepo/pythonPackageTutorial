#!/usr/local/bin/python
# -*- coding:utf-8 -*-

import logging

# 一些重要的概念
# Logger 记录器，暴露了应用程序代码能直接使用的接口。
# Handler 处理器，将（记录器产生的）日志记录发送至合适的目的地。
# Filter 过滤器，提供了更好的粒度控制，它可以决定输出哪些日志记录。
# Formatter 格式化器，指明了最终输出中日志记录的布局。


# Logger记录器
# Logger是一个树形层级结构，在使用接口debug，info，warn，error，critical之前
# 必须创建Logger实例，即创建一个记录器，如果没有显式的进行创建，
# 则默认创建一个root logger，并应用默认的日志级别(WARN)，
# 处理器Handler(StreamHandler，即将日志信息打印输出在标准输出上)，
# 和格式化器Formatter(默认的格式即为第一个简单使用程序中输出的格式)。
logger_name = 'example'
handler_name = 'defaultHandler'
logger = logging.getLogger(logger_name)
# 创建Logger实例后，可以使用以下方法进行日志级别设置，增加处理器Handler。
logger.setLevel(logging.ERROR) # 设置日志级别为ERROR，即只有日志级别大于等于ERROR的日志才会输出
logger.addHandler(handler_name) # 为Logger实例增加一个处理器
logger.removeHandler(handler_name) # 为Logger实例删除一个处理器


# Handler处理器
# Handler处理器类型有很多种，比较常用的有三个，StreamHandler，FileHandler，NullHandler
# 创建StreamHandler之后，可以通过使用以下方法设置日志级别，设置格式化器Formatter，增加或删除过滤器Filter。
formatter_name = 'default_formatter'
filter_name = 'default_filter'
sh = logging.StreamHandler()
sh.setLevel(logging.WARN) # 指定日志级别，低于WARN级别的日志将被忽略
sh.setFormatter(formatter_name) # 设置一个格式化器formatter
sh.addFilter(filter_name) # 增加一个过滤器，可以增加多个
sh.removeFilter(filter_name) # 删除一个过滤器

# FileHandler
filename = 'default'
fh = logging.FileHandler(filename, mode='a', encoding=None, delay=False)

# NullHandler
# NullHandler类位于核心logging包，不做任何的格式化或者输出。
# 本质上它是个“什么都不做”的handler，由库开发者使用。


# Formatter 格式化器
# 使用Formatter对象设置日志信息最后的规则、结构和内容，默认的时间格式为%Y-%m-%d %H:%M:%S。
formatter = logging.Formatter(fmt=None, datefmt=None)
# 其中，fmt是消息的格式化字符串，datefmt是日期字符串。
# 如果不指明fmt，将使用'%(message)s'。
# 如果不指明datefmt，将使用ISO8601日期格式。

# Filter过滤器
# Handlers和Loggers可以使用Filters来完成比级别更复杂的过滤。
# Filter基类只允许特定Logger层次以下的事件。
# 例如用‘A.B’初始化的Filter允许Logger 
# ‘A.B’, ‘A.B.C’, ‘A.B.C.D’, ‘A.B.D’等记录的事件，
# logger‘A.BB’, ‘B.A.B’ 等就不行。
#  如果用空字符串来初始化，所有的事件都接受。
filter = logging.Filter(name = '')

# Python Package Tutorial
这个README介绍了python开发项目时，绕不开的，需要掌握的一些重要包

## logging
+ logging模块使用过程
    1. 第一次导入logging模块或使用reload函数重新导入logging模块，logging模块中的代码将被执行，这个过程中将产生logging日志系统的默认配置。
    2. 自定义配置(可选)。logging标准模块支持三种配置方式: dictConfig，fileConfig，listen。其中，dictConfig是通过一个字典进行配置Logger，Handler，Filter，Formatter；fileConfig则是通过一个文件进行配置；而listen则监听一个网络端口，通过接收网络数据来进行配置。当然，除了以上集体化配置外，也可以直接调用Logger，Handler等对象中的方法在代码中来显式配置。
    3. 使用logging模块的全局作用域中的getLogger函数来得到一个Logger对象实例(其参数即是一个字符串，表示Logger对象实例的名字，即通过该名字来得到相应的Logger对象实例)。
    4. 使用Logger对象中的debug，info，error，warn，critical等方法记录日志信息。

+ logging的自定义配置
    + 文件配置
        + 参考代码`logger_fileconfig.py`
    + 字典配置
        + 可以使用`logging.config.dictConfig(config)`编写一个示例程序
    + 监听配置
        + 可以使用`logging.config.listen(port=DEFAULT_LOGGING_CONFIG_PORT)`编写一个示例程序

+ Logger是一个树形层级结构;
    + Logger可以包含一个或多个Handler和Filter，即Logger与Handler或Fitler是一对多的关系;
    + 一个Logger实例可以新增多个Handler，一个Handler可以新增多个格式化器或多个过滤器，而且日志级别将会继承。
![](/pic/element_relation.jpg.png)

+ Logging模块处理流程
    + 判断日志的等级是否大于Logger对象的等级，如果大于，则往下执行，否则，流程结束。
    + 产生日志。第一步，判断是否有异常，如果有，则添加异常信息。第二步，处理日志记录方法(如debug，info等)中的占位符，即一般的字符串格式化处理。
    + 使用注册到Logger对象中的Filters进行过滤。如果有多个过滤器，则依次过滤；只要有一个过滤器返回假，则过滤结束，且该日志信息将丢弃，不再处理，而处理流程也至此结束。否则，处理流程往下执行。
    + 在当前Logger对象中查找Handlers，如果找不到任何Handler，则往上到该Logger对象的父Logger中查找；如果找到一个或多个Handler，则依次用Handler来处理日志信息。但在每个Handler处理日志信息过程中，会首先判断日志信息的等级是否大于该Handler的等级，如果大于，则往下执行(由Logger对象进入Handler对象中)，否则，处理流程结束。
    + 执行Handler对象中的filter方法，该方法会依次执行注册到该Handler对象中的Filter。如果有一个Filter判断该日志信息为假，则此后的所有Filter都不再执行，而直接将该日志信息丢弃，处理流程结束。
    + 使用Formatter类格式化最终的输出结果。 注：Formatter同上述第2步的字符串格式化不同，它会添加额外的信息，比如日志产生的时间，产生日志的源代码所在的源文件的路径等等。
    + 真正地输出日志信息(到网络，文件，终端，邮件等)。至于输出到哪个目的地，由Handler的种类来决定。
![](/pic/logging_flow.png)

+ 参考资料
    + [英文Python logging HOWTO](https://docs.python.org/2/howto/logging.html#logging-basic-tutorial)
    + [中文Python 日志 HOWTO](http://python.usyiyi.cn/python_278/howto/logging.html#logging-basic-tutorial)
    + [Python日志系统Logging](http://www.52ij.com/jishu/666.html)
    + [logging模块学习笔记：basicConfig配置文件](http://www.cnblogs.com/bjdxy/archive/2013/04/12/3016820.html)
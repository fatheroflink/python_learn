#! /usr/bin/env python


'''
    对象的三个特性
    1.身份: 唯一标识, 可使用内建函数id()获得, 可被认为是对象内存地址
    2.类型: 决定对象可以保存什么类型的值
    3.值: 对象数据项
'''


'''
    标准类型, 基本数据类型
    Integer
    Boolean
    Long Integer
    Floating point real number
    Complex number
    String
    List
    Tuple
    Dictionary
'''

'''
    其它内建类型
    None
    文件
    set
    function
    module
    class
'''


'''
    内部类型
    code    python源代码片段,可执行对象,调用compile()可得到, 可以被exec命令或eval()内建函数执行
    frame   python执行栈帧, 包含解释器运行时所有信息
    trace record    异常发生时,包含针对异常的跟踪记录对象被创建
    slice   使用切片语法时创建
    Xrange
'''


'''
    内建函数
    cmp(obj1, obj2): 根据比较结果返回整型
    repr(obj)   对象字符串表示
    str(obj)    对象适合可读性好的字符串表示
    type(obj)   对象类型
'''


'''
    类型工厂函数
    int(), long(), float(), complex()
    type()
    list(), tuple()
    str(), unicode(), basestring()

    dict()
    bool()
    set(), frozenset()
    object(),
    classmethod(),
    staticmethod(),
    super(),
    property(),
    file()
'''
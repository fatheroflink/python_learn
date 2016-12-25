#! /usr/bin/env python
#encoding=utf8


'''
    #: python注释
    \n: 标准换行符
    \: 继续上一行
    ;: 两个语句链接在一行
    :: 代码头和体分开
    block: 用缩进体现
'''


'''
    \:
    单一语句, 含有(), [], {}可多行
    三括号下可多行
'''


'''
    支持多重赋值
'''
a = b = c = 1
print a, b, c


'''
    支持多元赋值
'''
x, y, z = 1, 2, 'zhangsan'
print x, y, z

x, y = y, x
print x, y
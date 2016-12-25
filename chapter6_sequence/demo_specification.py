#! /usr/bin/env python
#encoding=utf8

'''
    序列类型操作符
    1. in, not in
    2. +, 不是最快的, 字符串最好用 join, 列表最好用extend用于合并
    3. *, 多个拷贝
    4. :, 切片
    5. 步长索引
'''

s = 'abcdefg'
print s[::-1]
print s[::]


raw = r'\nsdiwe\t'
print raw
#!/usr/bin/env python


file = open("../data/data1.txt", mode='r', buffering=-1)

content = file.read(2)
print content

file.readline()

file.seek(0, whence=-1)

file.tell()

file.read()

file.readline(size=-1)

file.readlines()

file.xreadlines()

file.close()

file.write("str")

file.writelines("lines")

file.flush()


file.mode

file.closed

file.encoding

file.name

file.newlines

file.softspace



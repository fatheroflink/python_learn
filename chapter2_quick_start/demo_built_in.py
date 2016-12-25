#! /usr/bin/env python


file1 = open("../data/data2.txt")
set1 = set()
for line in file1:
    set1.add(line.strip())

file2 = open("../data/data1.txt")

for line in file2:
    if line.strip() not in set1:
        print line.strip()


'''
    access_mode:
    'r', 'w', 'a', 'b'
'''
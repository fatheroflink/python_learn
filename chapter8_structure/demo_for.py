#!/usr/bin/env python
import math



count = 0

while count < 10:
    count += 1
    if count == 9:
        break
else:
    print count


l = [1, 3,4, 5,5]

print ",".join("\"%s\"" % i for i in l)
print type("\"%s\"" % i for i in l)
print math.sin(52.0/180)

print type(["\"%s\"" % i for i in l])
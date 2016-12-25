#!/usr/bin/env python
#encoding=utf8


# list = ['a', 'b', 'c']
#
# print ",".join(list)
#
# del list[1]
print list

'''
    append(ele),
    insert(
'''


# list =  [i for i in range(10) if i % 2 == 0]
# print list.count(2)
# print list.index(2)
# list.insert(3, 20)
# list.remove(20)
# print list
# list.reverse()
# print list


person = ['name', ['savings', 100.00]]

hubby = person[:]

print hubby

wifey = list(person)

print "wifey: %s" % wifey

print [id(x) for x in person, hubby, wifey]

l = [('a', 23), ('b', 23342), ('c', 342)]
d = dict(l)

print d.keys()
print d.values()
print d.items()

d2 = {
    'a': 1234,
    'e': 4332
}

d.update(d2)
print d


s1 = set()
s1.add("a")
s1.add("b")
s1.add("c")


s2 = set()
s2.add("a")
s2.add("d")

print s1 | s2

print s1 - s2

print s1 & s2

print s1 ^ s2


s3 = set('1')
s2 |= s3
print s2
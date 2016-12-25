#! /usr/bin/env python


try:
    file = open("lla")
    for line in file:
        print line,
    file.close()
except Exception, e:
    print e

#!/usr/bin/env python


try:
    open("__init__.py")
except Exception, e:
    print e
else:
    print "else"
finally:
    print "finally"
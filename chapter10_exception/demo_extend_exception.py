#!/usr/bin/env python

class MyError(Exception):

    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)


try:
    raise MyError("asdf")
except MyError, e:
    print e.value


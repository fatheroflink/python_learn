#! /usr/bin/env python


class FooClass(object):

    '''
        static member declarations
         method declarations
    '''

    version = 0.1

    def __init__(self, nm='Join Doe'):
        self.name = nm
        print 'CREATE A CLASS INSTANCE FOR ', nm

    def showname(self):
        print 'your name is: ', self.name

    def showver(self):
        print self.version

    def addMe2Me(self, x):

        return x+x


if __name__ == "__main__":
    foo = FooClass('wang')
    print foo.showname()
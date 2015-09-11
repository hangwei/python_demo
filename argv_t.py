# -*- coding: utf-8 -*-

import sys

def argv_t():
    args = sys.argv
    if len(args) == 1:
        print 'Hello, world!'
    elif len(args)==2:
        print 'Hello, %s!' % args[1]
    else:
        print 'Too many arguments!'

if __name__ == '__main__':
    argv_t()

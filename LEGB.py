#!/usr/bin/env python
# -*- coding:utf-8 -*-

__builtins__.b = "builtins"

g = "glabals"

def enclose():
    e = "enclosing"
    def test():
        l = "locals"
        print l
        print e
        print g
        print b
    return test

if __name__ == "__main__":
    enclose()()

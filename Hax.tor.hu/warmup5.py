#! /usr/bin/env python
# coding: utf-8

start = 65
while True:
    num = [start+18, start+4, start+1, start+23]
    for i in xrange(0, 4):
        if num[i] > 122:
            num[i] = num[i]%122 + 65
    str1 = []
    for i in num:
        str1.append(chr(i))
    print ''.join(str1)
    start += 1
    if start == 123:
        break


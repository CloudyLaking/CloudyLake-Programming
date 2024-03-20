#!/usr/bin/python
# -*- coding: UTF-8 -*-

width = int(input('输入对角线长度：'))
for row in range(1,width+1):
    for col in range(1,width+1):
        if ((abs(row - (width+1)/2) + abs(col - (width+1)/2)) == (width-1)/2):
            print("*", end="")#这个end=""是因为python中print自带换行
        else:
            print(" ", end="")
    print()
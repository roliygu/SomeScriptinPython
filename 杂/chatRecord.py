#! /usr/bin/env python
#coding=gbk
import sys

#(origin ,num) = (sys.argv[1],int(sys.argv[2]))
(origin ,num) = ('test.txt',8)

def main():
    #删除的是第一到num-1行
    input = open(origin,'r')
    List = input.readlines()
    List = List[num-1:]
    input.close()
    output = open(origin,'w')
    output.writelines(List)
    output.close()

main()
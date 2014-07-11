#! /usr/bin/env python
#coding=utf-8
'''
一个列表表示一个兵种，对应项分别是，兵种名，每秒伤害值，
生命值，训练费用，所需空间，训练时间，移动速度
'''

Wizard = ["法师",125,130,3000,4,480,16]
Barbarian = ["野蛮人",23,95,100,1,20,16]
Archer = ["弓箭手",16,33,160,1,25,24]
Goblin = ["哥布林",24,43,80,1,30,32]
Giant = ["胖子",24,520,2000,5,120,12]
WallBreaker = ["炸弹人",32,35,2500,2,120,24]
Ballon = ["气球兵",48,216,3000,5,480,10]
Dragon = ["大龙",160,2100,30000,20,1800,16]
Healer = ["天使",42,600,6000,14,900,16]

LightNingSpell = 20000
HealingSpell = 20000
RageSpell = 25000

Spell = [LightNingSpell,HealingSpell,RageSpell]
Soldier = [Wizard,Barbarian,Archer,Goblin,Giant,WallBreaker,Ballon,Dragon,Healer]



def getSumIndex(index,Num):
    #得到index的向量和Num的积
    Temp = [i[index] for i in Soldier]
    sum = 0
    for i in range(len(Temp)):
        sum += Temp[i]*Num[i]  
    return sum

def show(Num):
    AllSum = [ getSumIndex(i,Num) for i in range(1,6)]
    AllSum[4]/=4
    min = AllSum[4]/60
    sec = AllSum[4]%60
    print " 伤害值: %d  生命值: %d  圣水: %d  空间: %d  " % tuple(AllSum[:-1]),
    print "时间: %d min %d s" % (min,sec)
    
Num = [4,32,24,28,12,10,0,0,0]
show()
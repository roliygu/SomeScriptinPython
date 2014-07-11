#! /usr/bin/env python
#coding=utf-8
import sys,os
sys.path+=[os.getcwd()]

file = open('.\\1.txt','r').readlines()
class Student:
	def __init__(self,add,school,ID,Name,Group,prize,vector = False):
		self.add = add
		self.school = school
		self.ID = ID
		self.Name = Name
		self.Group = Group
		self.prize = prize
		self.vector = vector
	def show(self):
		return (self.add,self.school,self.ID,self.Name,self.Group,self.prize,self.vector)
def ACK(L,i):
	if i+6<len(L):
		if len(L[i+6]) == 3:
			StuTemp = Student(L[i],L[i+1],L[i+2],L[i+3],
				L[i+4],L[i+5],True)
			return (i+7,StuTemp)
		else :
			StuTemp = Student(L[i],L[i+1],L[i+2],
				L[i+3],L[i+4],L[i+5])
			return (i+6,StuTemp)
L=[]
for i in file:
	if i[0] != "\n" and i[0]!= "" and i[0]!=' ':
		L.append(i[:-1])

def getTable(L):
	i=0
	Le = len(L)
	print Le
	Table = []
	while i+6<Le:
		(newi,newStu) = ACK(L,i)
		Table.append(newStu)
		i = newi
	return Table

def priAndNot(Table):
	count = 0
	for i in Table:
		if i.vector == True:
			count +=1
	return (count,len(Table))
T = getTable(L)
#print priAndNot(T)
out = open('.\\out.txt','wb')
def writt(fi,cl):
	fi.write(cl.add)
	fi.write(' ')
	fi.write(cl.school)
	fi.write(' ')
	fi.write(cl.ID)
	fi.write(' ')
	fi.write(cl.Name)
	fi.write(' ')
	fi.write(cl.Group)
	fi.write(' ')
	fi.write(cl.prize)
	fi.write(' ')
	fi.write(str(cl.vector))
	fi.write('\n')
for i in T:
	writt(out,i)
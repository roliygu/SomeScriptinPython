#! /usr/bin/env python
#coding=utf-8
FibNumber = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 
    233, 377, 610, 987, 1597, 2584, 4181, 6765, 
    10946, 17711, 28657, 46368, 75025]
    
T = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,
    79,83,89,97,101,103,107,109,113,127,131,137,139,149,151,157,163,
    167,173,179,181,191,193,197,199,211,223,227,229,233,239,241,251,
    257,263,269,271,277,281,283,293,307,311,313,317,331,337,347,349,
    353,359,367,373,379,383,389,397,401,409,419,421,431,433,439,443,
    449,457,461,463,467,479,487,491,499]
    
def sumOfChar(S):
    sum=0
    for i in range(len(S)):
        sum += ord(S[i])
    return sum

def Fib(Num):
    L = []
    while Num!=0:
        for i in range(20):
            if FibNumber[i]<=Num and FibNumber[i+1]>Num:
                L.append(FibNumber[i])
                Num-=FibNumber[i]
                break
    return L

def getFibpassword(L,num,Len):
    st = ''
    if Len == 2:
        return chr((L[0]*num)%26+65)+chr((L[1]*num)%26+97)
    elif Len == 5:
        for i in range(5):
            index = i%len(L)
            if index%2==0:
                st+=chr((L[index]*num)%26+65)
            else:
                st+=chr((L[index]*num)%26+97)
            num+=2
        return st
    else:
        for i in range(7):
            index = i%len(L)
            if index%2==0:
                st+=chr((L[index]*num)%26+65)
            else:
                st+=chr((L[index]*num)%26+97)
            num+=3
        return st
            
def PrimNum(Num):
    Num=Num%500
    L = []
    while Num!=1:
        for i in range(95):
            if Num%T[i]==0:
                L.append(T[i])
                Num /=T[i]
                break
    L.reverse()
    return L

def getpassword(add,password,number,Len):
    if Len==6:
        return getFibpassword(PrimNum(sumOfChar(add)),number,2)+getFibpassword(Fib(sumOfChar(password)),number,2)+chr(number%10+48)
    elif Len==12:
        return getFibpassword(PrimNum(sumOfChar(add)),number,5)+getFibpassword(Fib(sumOfChar(password)),number,5)+str(number)
    else:
        return getFibpassword(PrimNum(sumOfChar(add)),number,7)+getFibpassword(Fib(sumOfChar(password)),number,7)+str(number)


passwordseed = 'gurui111'
xuetangX = ["http://www.xuetangx.com/",7,12]
xiaomi = ["http://www.mi.com/",3,12]
print 'xuetangX : ',getpassword(xuetangX[0],passwordseed,xuetangX[1],xuetangX[2])
print 'xiaomi : ',getpassword(xiaomi[0],passwordseed,xiaomi[1],xiaomi[2])
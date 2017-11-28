import sys
sys.setrecursionlimit(6650)
import math
from math import *
import pprint
from pprint import *
ab=[4,6]

def Dioph1(d,m):
    i=0
    summ=0
    while i<len(m):
        summ+=m[i]
        i+=1
    j=0
    summ2=0
    while j<len(m):
        summ2+=(m[j]*m[j])
        j+=1
    if 3*d-1==summ and d*d+1==summ2:
        return True

Dioph1(16,[6,6,6,6,6,6,6,1,1,1,1,1])

def MoreDioph(a,b,m):
    i=0
    summ=0
    while i<len(m):
        summ+=m[i]
        i+=1
    j=0
    summ2=0
    while j<len(m):
        summ2+=(m[j]*m[j])
        j+=1
    if a>=summ and b>=summ2:
        return True
    
def EqDioph(a,b,m):
    i=0
    summ=0
    while i<len(m):
        summ+=m[i]
        i+=1
    j=0
    summ2=0
    while j<len(m):
        summ2+=(m[j]*m[j])
        j+=1
    if a==summ and b==summ2:
        return True

# print(EqDioph(17,37,[3,2,2,2,2,2,2,2]))

def rek4(ga,gb,a=-1,b=-1,m=-1,M=[],L=[],k=0):
    k+=1
    if EqDioph(ga,gb,M)==True and M not in L:
        GM=M.copy()
        print(M)
        L.append(GM)        
    if len(M)==1:
        if M[0]==1:
            print(L)
            return L
    if m==-1 and b==-1 and a==-1:
        m=trunc(sqrt(gb))
        a=ga
        b=gb
        rek4(ga,gb,a,b,m,M,L,k)
    elif m>1:
        if a>=m and b>=m*m:
            M.append(m)
            rek4(ga,gb,a-m,b-m*m,m,M,L,k)
        else:
            rek4(ga,gb,a,b,m-1,M,L,k)
    elif m==1:
        if a>=m and b>=m*m:
            M.append(m)
            rek4(ga,gb,a-m,b-m*m,m,M,L,k)
        else:
            M.append(m)
            M=M[:M.index(1)]
            m=M[-1]-1
            M[-1]=m
            i=0
            s=0
            s2=0
            while i<len(M):
                s+=M[i]
                s2+=M[i]*M[i]
                i+=1
            a=ga-s
            b=gb-s2
            rek4(ga,gb,a,b,m,M,L,k)



print(rek4(17,37))

#print(rek4(47,257))

                




    

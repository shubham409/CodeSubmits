from math import floor,ceil
from collections import Counter

def fun(ls):
    prv=None
    count=0
    for i,val in enumerate(ls):
        if(i==0):
            prv=val
            continue
        if(val>2*prv):
            # current number is bigger than twice of previous
            # insert 2*prv at i
            ls.insert(i,2*prv)
            prv=2*prv
            count+=1
            continue
        if(prv>2*val):
            # previous number is bigger than twicw of this number
            # insert half of previos 
            ls.insert(i,ceil(prv/2))
            prv=ceil(prv/2)
            count+=1
            continue
        prv=val
    print(count)

T= int(input())
for i in range(T):
    t= int(input())
    ls= list(map(int,input().split()))
    fun(ls)

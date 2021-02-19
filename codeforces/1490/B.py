from math import floor
from collections import Counter
def fun(ls):
    lt= [i%3 for i in ls]
    dct= Counter(lt)
    if (dct.get(0)==None):
        dct[0]=0
    if (dct.get(1)==None):
        dct[1]=0
    if (dct.get(2)==None):
        dct[2]=0
    c0=dct.get(0)
    c1=dct.get(1)
    c2=dct.get(2)
    # print(c0,c1,c2)
    count=0
    what_should_be= (c0+c1+c2)//3
    while(not (c1 ==c2==c0)):
        if(c0>c1):
            c0=c0-1
            c1=c1+1
            count+=1
            continue
        if(c1>c2):
            c1=c1-1
            c2=c2+1
            count+=1
            continue
        if(c2>c0):
            c2=c2-1
            c0=c0+1
            count+=1
    print(count)
    
T= int(input())
for i in range(T):
    t= int(input())
    ls= list(map(int,input().split()))
    fun(ls)
 
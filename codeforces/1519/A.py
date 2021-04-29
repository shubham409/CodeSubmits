from math import ceil

def fun(ls):
    a,b,c=ls
    mn=min(a,b)
    a=a-mn
    b=b-mn
    if(a>0):
        avg=ceil(a/mn)
        if(avg<=c):
            print('Yes')
        else:
            print('No')
    else:
        avg=ceil(b/mn)
        if(avg<=c):
            print('Yes')
        else:
            print('No')

T = int(input())
for i in range(T):
    ls= list(map(int, input().split()))
    fun(ls)
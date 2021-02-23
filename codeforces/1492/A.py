from math import ceil
from decimal import Decimal
def fun(ls):
    p,a,b,c =ls
    ta=(ceil(Decimal(p)/Decimal(a))*a)
    tb=(ceil(Decimal(p)/Decimal(b))*b)
    tc=(ceil(Decimal(p)/Decimal(c))*c)
    # print(Decimal(p)/Decimal(a))
    print(min(ta,tb,tc)-p)


T= int(input())
for i in range(T):
    ls=list(map(int,input().split()))
    # ls= input()
    fun(ls)
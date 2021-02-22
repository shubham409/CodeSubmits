from collections import Counter 
from math import ceil

def fun(ls,lt):
    n,x=lt
    mx=[ceil(i/x)for i in ls]
    mx_value=(sum(mx))
    print(ceil(sum(ls)/x),mx_value)
T= int(input())
for i in range(T):
    lt= list(map(int,input().split()))
    ls= list(map(int,input().split()))
    fun(ls,lt)
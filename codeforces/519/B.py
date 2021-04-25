from collections import Counter
from math import ceil
from decimal import Decimal

def fun(a,b,c):
    dct1=Counter(a)
    dct2=Counter(b)
    dct3=Counter(c)
    k=list(dct1.items()-dct2.items())
    print((k[0][0]))
    k=list(dct2.items()-dct3.items())
    print((k[0][0]))


        

T = int(input())
T=1
for i in range(T):
    # var=input()
    # st=input()
    # val=int(input())
    # ks= list(map(int, input().split()))
    # ms= list(map(int, input().split()))
    # ls= list(map(int, input().split()))
    ks= list(map(int, input().split()))
    ls= list(map(int, input().split()))
    ms= list(map(int, input().split()))
    fun(ks,ls,ms)
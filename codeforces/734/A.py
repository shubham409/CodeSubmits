from collections import Counter
from math import ceil
def fun(ls):
    dct=Counter(ls)
    A=dct.get('A')
    D=dct.get('D')
    if ( A==None):
        dct['A']=0
    if (D==None):
        dct['D']=0
    A=dct.get('A')
    D=dct.get('D')
    if(A>D):
        print("Anton")
    if(A<D):
        print("Danik")
    if(A==D):
        print("Friendship")





# T=int(input())
# for i in range(T):
#     ls= list(map(int,input().split()))
#     fun(ls)
t=input()
t=input()
fun(t)
from collections import Counter
from itertools import zip_longest

# cook your dish here
def fun(ls,q):
    dct =Counter(ls)
    # one = 0 if dct.get(1)==None else dct.get(1)
    # zero= 0 if dct.get(0)==None else dct.get(0)
    if(dct.get(0)==None):
        dct[0]=0
    if (dct.get(1)== None):
        dct[1]=0
    for i in range(q):
        typeop,xork = list(map(int,input().split()))
        if(typeop== 1):
            x=xork
            get= ls[x-1]
            ls[x-1]=1-ls[x-1]
            if get==0:
                dct[0]=dct.get(0)-1
                dct[1]=dct.get(1)+1
            else:
                dct[1]=dct.get(1)-1
                dct[0]=dct.get(0)+1
        else:
            k=xork
            if(dct.get(1)>=k):
                print(1)
            else:
                print(0)
        # print(ls,dct.get(1),dct.get(0))

# T= int(input())
# for i in range(T):
n,q=list(map(int,input().split()))
ls=list(map(int,input().split()))
fun(ls,q)





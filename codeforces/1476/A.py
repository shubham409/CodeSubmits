from math import ceil
def fun(ls):
    n=ls[0]
    k=ls[1]
    if( n<= k ):
        print (ceil(k/n))
    else:
        if(k==1):
            print(1)
            return
        # n>k
        if(n%k==0):
            print(1)
            return
        else:
            print(2)
        # d=n//k
        # r=n%k
        # print(d+r)
        # print((ceil(n/k)*k-n))

T= int(input())
for i in range(T):
    # t= int(input())
    ls= list(map(int,input().split()))
    fun(ls)
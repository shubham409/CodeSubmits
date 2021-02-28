def fun(ls,u,v):
    if(len(set(ls))==1):
        print(v+min(v,u))
        return
    prv=ls[0]
    ans=0
    for i in ls[1::]:
        ans=max(ans,abs(i-prv))
        prv=i
    if(ans>=2):
        print(0)
    else:
        print(min(v,u))


T= int(input())
for i in range(T):
    # t= int(input())
    # n= int(input())
    # m= int(input())
    n,u,v= list(map(int,input().split()))
    ls= list(map(int,input().split()))
    fun(ls,u,v)
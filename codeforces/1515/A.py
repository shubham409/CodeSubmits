def fun(ls,ks):
    n,x=ks
    st=sorted(ls)
    sm=sum(ls)
    if(st[-1]>x):
        print("YES")
        print(*st[::-1])
        return
    if(sm<x):
        print("YES")
        print(*st)
        return
    if(sm==x):
        print("NO")
        return
    ans=[]
    prv=None
    leave=None
    for i in st:
        if prv==None:
            prv=i
        else:
            prv+=i
        if(prv==x):
            leave=i
        else:
            ans.append(i)
    if(leave==None):
        print('YES')
        print(*st)
    else:
        ans.append(leave)
        print('YES')
        print(*ans)
 

T = int(input())
for i in range(T):
    ks= list(map(int, input().split()))
    ls= list(map(int, input().split()))
    fun(ls,ks)
def fun(ls,ks):
    n,k=ks
    temp=k
    if(n==2):
        if(k>=ls[0]):
            prv=ls[0]
            ls[0]=0
            ls[1]=ls[1]+prv
        else:
            ls[0]=ls[0]-k
            ls[1]=ls[1]+k
        print(*ls)
        return
    sm=sum(ls[:-1])
    if(k<sm):
        for i,val in enumerate(ls):
            if(val<=k):
                ls[i]=0
                k=k-val
            else:
                ls[i]=val-k
                break
        ls[-1]=ls[-1]+temp
        print(*ls)
    else:
        print(*(([0]*(n-1))+([ls[-1]+sm])))

T = int(input())
for i in range(T):
    ks= list(map(int, input().split()))    
    ls= list(map(int, input().split()))    
    fun(ls,ks)
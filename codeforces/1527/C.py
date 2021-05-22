def fun(n,ls):
    dp=[0 for i in range(n)]
    dct={i:0 for i in ls}
    ans=0
    for i in range(n):
        if(i>0):
            dp[i]=dp[i-1]
        if(ls[i] in dct):
            dp[i]+=dct.get(ls[i])
        dct[ls[i]]+=i+1
        ans+=dp[i]
    print(ans)


T = int(input())
for i in range(T):
    n=int(input())
    ls= list(map(int, input().split()))
    fun(n,ls)



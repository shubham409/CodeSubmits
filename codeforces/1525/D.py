def fun(n,st):
    one=[]
    zero=[]
    one_len=0
    zero_len=0
    for i,val in enumerate(st):
        if(val==1):
            one.append(i)
            one_len+=1
        else:
            zero.append(i)
            zero_len+=1

    if(one_len==0):
        print(0)
        return

    dp=[[10**12 for i in range(zero_len)]for j in range(one_len)]
    for i in range(one_len):
        for j in range(i,zero_len):
            if(i==0):
                if(j==0):
                    dp[i][j]=abs(one[i]-zero[j])
                else:
                    dp[i][j]=min(dp[i][j-1],abs(one[i]-zero[j]))
            else:
                dp[i][j]=min(dp[i][j-1],dp[i-1][j-1]+abs(one[i]-zero[j]))
    print(dp[one_len-1][zero_len-1])



T=1
for i in range(T):
    n=int(input())
    ls= list(map(int, input().split()))
    fun(n,ls)
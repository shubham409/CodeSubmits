from collections import Counter
def fun(ls):
    dct= Counter(ls)
    mx=max(dct.keys())
    for i in range(mx+1):
        if(dct.get(i)==None):
            dct[i]=0
    # ans=get(mx,dct)
    # print(ans)
    dp=[]
    dp.append(0)
    dp.append(dct[1])
    for i in range(2,mx+1):
        dp.append(max(dct[i]*i+ dp[i-2],dp[i-1]))
    print(dp[-1])

        
t= input()
ls= list(map(int,input().split()))
fun(ls)
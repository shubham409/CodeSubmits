def fun(ls,n):
    ans=0
    prv=True
    # true means last num was + false means last num was -
    num=0
    for i in ls:
        val=i
        if(i<0):
            if(prv):
                ans+=num
                num=val
            else:
                num=max(val,num)
            prv=False
        else:
            if(prv):
                num=max(val,num)  
            else:                
                ans+=num
                num=val
            prv=True
    ans+=num
    print(ans)



    
T = int(input())
for _ in range(T):
    n=list(input())
    ls= list(map(int, input().split()))
    fun(ls,n)
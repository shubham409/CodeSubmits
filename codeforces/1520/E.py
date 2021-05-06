def fun(st,n):
    suffix=[0 for i in range(n)]
    prefix=[0 for i in range(n)]
    count=0
    for i,val in enumerate(st):
        if(val=='*'):
            if(i==0):
                prefix[i]=0
                count+=1
            else:
                prefix[i]=prefix[i-1]
                count+=1
        else:
            if(i==0):
                prefix[i]=0
                count+=0
            else:
                prefix[i]=prefix[i-1]+count
                count+=0
    count=0
    for i in range(n-1,-1,-1):
        val=st[i]
        if(val=='*'):
            if(i==n-1):
                suffix[i]=0
                count+=1
            else:
                suffix[i]=suffix[i+1]
                count+=1
        else:
            if(i==n-1):
                suffix[i]=0
                count+=0
            else:
                suffix[i]=suffix[i+1]+count
                count+=0
    ans=10**12
    for i in range(n):
        if(i!=n-1):
            ans=min(ans,prefix[i]+suffix[i+1])
        else:
            ans=min(ans,prefix[i])
    print(ans)

T = int(input())
for _ in range(T):
    n=int(input())
    st=input()
    fun(st,n)
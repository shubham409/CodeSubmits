def fun(n):
    count=1
    ans=0
    for i in range(3,n+1):
        if(i%2!=0):
            ans+=(4*(i-1)*count)
            count+=1
    print(ans)
    

T = int(input())
for i in range(T):
    val=int(input())
    fun(val)
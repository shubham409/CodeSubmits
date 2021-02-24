def fun(num:int):
    temp=num
    ans=''
    if (num>45):
        print(-1)
        return
    i=9
    while(num>0):
        if(num>i):
            ans+=str(i)
            num=num-i
            i-=1
        else:
            ans+=str(num)
            num=0
    print((ans[-1::-1]))


    
T= int(input())
for i in range(T):
    t= int(input())
    # ls= list(map(int,input().split()))
    # fun(ls)
    fun(t)
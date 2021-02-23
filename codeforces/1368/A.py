def fun(ls):
    x,y,n=ls
    count=0
    a=max(x,y)
    b=min(x,y)

    while(a<= n and b<=n):
        tempb=b
        tempa=a
        b=tempa
        a=tempa+tempb
        count+=1
    print(count)




T= int(input())
for i in range(T):
    # t= int(input())
    ls= list(map(int,input().split()))
    fun(ls)
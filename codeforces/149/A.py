def fun(ls,n):
    st=sorted(ls,reverse=True)
    target=0
    count_month=0
    for i in st:
        if(target>=n):
            break
        else:
            target+=i
            count_month+=1
    if(target>=n):
        print(count_month)
    else:
        print(-1)

T=1
for i in range(T):
    n=int(input())
    ls= list(map(int, input().split()))    
    fun(ls,n)
def fun(n,ls):
    ans=0
    for i in range(n):
        mid_zero=0
        mid_one=0
        for j in range(i,n):
            after_one=0
            before_one=0
            if(ls[j]==1):
                mid_one+=1
            else:
                mid_zero+=1
            for k in range(j+1,n):
                if(ls[k]==1):
                    after_one+=1
            for k in range(0,i):
                if(ls[k]==1):
                    before_one+=1            
            ans=max(ans,mid_zero+after_one+before_one)
    print(ans)


T=1
for i in range(T):
    n=int(input())
    ls= list(map(int, input().split()))
    fun(n,ls)
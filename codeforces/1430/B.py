def fun(ls,k):
    k=k+1
    lt=sorted(ls)[::-1]
    ans=0
    count=0
    for i in lt:
        ans+=i
        count+=1
        if(count>=k):
            break
    print(ans)

        

T = int(input())
for i in range(T):
    n,k = list(map(int, input().split()))
    ls = list(map(int, input().split()))
    fun(ls,k)
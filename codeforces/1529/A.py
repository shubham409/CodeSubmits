def fun(n,ls):
    st=sorted(ls)
    first=st[0]
    ans=0
    count=0
    for i in st:
        if(first==i):
            count+=1
        else:
            break
    print(n-count)

T = int(input())
for i in range(T):
    n=int(input())
    ls= list(map(int, input().split()))
    fun(n,ls)
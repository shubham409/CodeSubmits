def fun(ls,n):
    mn=min(ls)
    for i in ls:
        if (i-mn)%2!=0:
            print('NO')
            return
    print('YES')


    
T = int(input())
for _ in range(T):
    n=list(input())
    ls= list(map(int, input().split()))
    fun(ls,n)
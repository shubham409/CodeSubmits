def fun(n):
    print(n)
    print(*range(1,n+1))
    

T= int(input())
for i in range(T):
    t= int(input())
    # ls= list(map(int,input().split()))
    fun(t)
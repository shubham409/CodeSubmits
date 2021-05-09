def fun(ls):
    a,b=ls
    if(b>=2*a):
        print(a,2*a)
    else:
        print(-1,-1)

T = int(input())
for _ in range(T):
    ls= list(map(int, input().split()))
    fun(ls)

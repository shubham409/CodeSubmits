def fun(ls):
    l = reversed(ls)
    print(*l)
T = int(input())
for i in range(T):
    ls= input().split()
    ls = list(map(int, ls ))
    ls= input().split()
    ls = list(map(int, ls ))
    fun(ls)
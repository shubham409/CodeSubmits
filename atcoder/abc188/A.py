def fun(ls):
    mn= min(ls)
    mx=max(ls)

    if mn+3>mx:
        print('Yes')
        return
    print('No')
# T= int(input())
T=1
for i in range(T):
    ls= list(map(int,input().split()))
    fun(ls)
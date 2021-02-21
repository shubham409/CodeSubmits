def fun(ls,d):
    ls=sorted(ls)
    if(ls[-1]<=d):
        print('yes')
        return
    if(ls[0]+ls[1]<=d):
        print('yes')
        return
    print('no')

T= int(input())
for i in range(T):
    n,d=list(map(int,input().split()))
    ls= list(map(int,input().split()))
    fun(ls,d)

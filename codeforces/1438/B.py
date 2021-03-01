def fun(ls):
    if(len(set(ls))<len(ls)):
        print('yes')
    else:
        print('no')






T= int(input())
for i in range(T):
    t= int(input())
    # n= int(input())
    # m= int(input())
    # n,u,v= list(map(int,input().split()))
    ls= list(map(int,input().split()))
    fun(ls)
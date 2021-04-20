def fun(ls):
    a=ls[0]
    b=ls[1]
    c=ls[2]
    d=ls[3]
    val256=min(a,c,d)
    a-=val256
    c-=val256
    d-=val256
    val32=min(b,a)
    print(val256*256+val32*32)


# T = int(input())
T=1
for i in range(T):
    # var=input()
    # val=int(input())
    # st=input()
    # ms= list(map(int, input().split()))
    ls= list(map(int, input().split()))
    # ls= list(input())
    # qs=list(map(int, input().split()))
    fun(ls)
def fun(st,n):
    l=0
    r=0
    for i in st:
        if(i=='L'):
            l+=1
        else:
            r+=1
    print(l+r+1)
    


# T = int(input())
T=1
for i in range(T):
    # var=input()
    val=int(input())
    st=input()
    # ms= list(map(int, input().split()))
    # ls= list(map(int, input().split()))
    # ls= list(input())
    # qs=list(map(int, input().split()))
    fun(st,val)
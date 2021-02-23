def fun(st):
    if(st==1):
        print(0)
    if(st==2):
        print(1)
    if (st==3):
        print(2)
    if(st>3):
        if(st%2==0):
            print(2)
        else:
            print(3)
        

T= int(input())
for i in range(T):
    # t= int(input())
    # ls= list(map(int,input().split()))
    # fun(ls)

    st= int(input())
    fun(st)

     
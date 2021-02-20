def fun(st):
    if(st%2021==0 or st%2020==0):
        print('yes')
        return
    # a+b
    d=st/2020
    # b
    r=st%2020
    b=r
    a=d-r

    if(d>r):
        print('yes')
    else:
        print('no')

    



T= int(input())
for i in range(T):
    # t= int(input())
    # ls= list(map(int,input().split()))
    st= input()
    fun(int(st))
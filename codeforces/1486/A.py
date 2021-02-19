def fun(t,ls):
    ind=0
    value_sum=0
    i_sum=0
    for i,val in enumerate(ls):
        value_sum+=val
        i_sum+=i
        if(value_sum>=i_sum):
            ind=i
        else:
            print('no')
            return
    print('yes')


T= int(input())
for i in range(T):
    t= int(input())
    ls= list(map(int,input().split()))
    fun(t,ls)

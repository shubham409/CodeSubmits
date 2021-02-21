def fun(st,n):
    # if(st=='1' or st=='0'):
    #     print('1')
    #     return
    ans=''
    prv_sum=None
    for i,val in enumerate(st):
        val=int(val)
        if(val== 1):
            if(prv_sum==None or prv_sum==1 or prv_sum==0):
                prv_sum=2
                ans+='1'
                continue
            if(prv_sum==2):
                prv_sum=1
                ans+='0'
                continue
        else:
            if(prv_sum==2 or prv_sum==None or prv_sum==0):
                prv_sum=1
                ans+='1'
                continue

            if(prv_sum==1):
                prv_sum=0
                ans+='0'
    print(ans)





    

T= int(input())
for i in range(T):
    n=list(map(int,input().split()))
    ls= input()
    fun(ls,n)

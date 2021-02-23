def fun(st):
    if(st=='2020'):
        print('yes')
        return
    if((st[0] =='2' and st[-3:]=='020') or (st[:2]=='20' and st[-2:]=='20') or (st[:3]=='202' and st[-1]=='0')):
        print('yes')
        return
    if(st[:4]=='2020' or st[-4:]=='2020'):
        print('yes')
        return
    print('no')        
T= int(input())
for i in range(T):
    t= int(input())
    # ls= list(map(int,input().split()))
    st= input()
    # t= input()
    fun(st)
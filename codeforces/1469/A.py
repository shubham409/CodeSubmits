def fun(st):
    if(st[0]==')' or st[-1]=='(' or len(st)%2!=0):
        print('no')
        return
    print('yes')


T = int(input())
for i in range(T):
    # ls=list(map(int,input().split()))
    st = input()
    fun((st))

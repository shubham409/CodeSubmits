def fun(ls):
    a,b=sorted(ls)
    if(b%a==0):
        print('YES')
    else:
        print('NO')


T = int(input())
# T=1
for i in range(T):
    # n=int(input())
    # st=input()
    # ts=input()
    # ks= list(map(int, input().split()))    
    # ls= list(map(int, input().split()))    
    ls= list(map(int, input().split()))    
    fun(ls)
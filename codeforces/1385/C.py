def fun(ls,n):
    i=n-1
    while(i>0 and ls[i-1]>=ls[i]):
        i-=1
    while(i>0 and ls[i-1]<=ls[i]):
        i-=1
    print(i)
        
    
    

T = int(input())
for i in range(T):
    # n,k= list(map(int, input().split()))
    n=int(input())
    ls= list(map(int, input().split()))
    # ls=int(input())
    fun(ls,n)
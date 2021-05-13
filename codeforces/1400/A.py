def fun(st,n): 
    print(st[n-1]*n)

T = int(input())
for i in range(T):
    n=int(input())
    st=input()
    fun(st,n)
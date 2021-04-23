def fun(n):
    count=0
    if(n%2050==0):
        st=(n//2050)
        st=str(st)
        for i in st:
            count+=int(i)
        print(count)
    else:
        print(-1)
T = int(input())
for i in range(T):
    val=int(input())
    fun(val)
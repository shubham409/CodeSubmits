def fun(n):
    if(n==1):
        print(1)
        return
    if(n==2):
        print(-1)
        return
    ls=[[0 for j in range(n)] for i in range(n)]
    value=1
    for i in range(n):
        for j in range(0,n,2):
            if(i%2!=0):
                j=j+1
            if(j<n):
                ls[i][j]=value
                value+=1
    for i in range(n):
        for j in range(0,n,2):
            if(i%2==0):
                j=j+1
            if(j<n):
                ls[i][j]=value
                value+=1
    for i in ls:
        print(*i)   



T = int(input())
for _ in range(T):
    n=int(input())
    fun(n)
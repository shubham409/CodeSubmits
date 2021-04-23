def fun(ls,n,m):
    ans=ls
    show=[[]for _ in range(n)]
    count=m
    while count>0:
        mn=10**10
        mn_index=-1
        for i in range(n):
            for j in range(count):
                if(mn>ans[i][j]):
                    mn=ans[i][j]
                    mn_index=[i,j]

        for i in range(n):
            if(i!=mn_index[0]):
                mx=-1
                mx_index=-1
                for j in range(count):
                    if(mx<ans[i][j]):
                        mx=ans[i][j]
                        mx_index=[i,j]
                ans[i].pop(mx_index[1])
                show[i].append(mx)
            else:
                ans[mn_index[0]].pop(mn_index[1])
                show[mn_index[0]].append(mn)                
        count-=1
    for i in show:
        print(*i)

T = int(input())
for i in range(T):
    n,m= list(map(int, input().split()))
    ls=[]
    for i in range(n):
        ks= list(map(int, input().split()))
        ls.append(ks)
    fun(ls,n,m)
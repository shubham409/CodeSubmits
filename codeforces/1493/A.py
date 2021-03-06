from math import ceil
def fun(ls):
    n,k=ls
    ans=[]
    if(n>k):
        for i in range(ceil(k/2) ,n+1):
            if(i!=k):
                ans.append(i)
        # temp= k-(n//2)
        # for i in range(temp+1,n//2):
        #     ls.append(i)
        if(len(ans)==1 and ans[0]==0):
            print(0)
            return
        print(len(ans))
        print(*reversed(ans))
    else:
        extra = k-n 
        for i in range(ceil(k/2) ,n+1):
            if(i!=k):
                ans.append(i)
        # for i in range(1,extra-1):
        #     ans.append(i)
        if(len(ans)==1 and ans[0]==0):
            print(0)
            return
        print(len(ans))
        print(*reversed(ans))        




T=int(input())
for i in range(T):
    ls= list(map(int,input().split()))
    fun(ls)
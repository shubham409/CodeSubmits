from collections import Counter

def fun(ls,n):
    ans=[]
    count=0
    for i,val in enumerate(ls):
        ans.append(val-i)
        
    ctr=Counter(ans)
    
    for key,val in ctr.items():
        if(val>=2):
            # count+=(ncr(val,2))
            count+=(val*(val-1)//2)
    print(count)

T = int(input())
for _ in range(T):
    n=int(input())
    ls= list(map(int, input().split()))
    fun(ls,n)


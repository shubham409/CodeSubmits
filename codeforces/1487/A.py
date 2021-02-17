def fun(ls):
    mn=min(ls)
    l=sorted(ls)
    count=0
    for i,val in enumerate(l[1:]):
        if(l[i-1]<val or val>mn ):
            # print(l[i-1],val,mn)
            count+=1
    print(count)


T= int(input())
for i in range(T):
    t= int(input())
    ls= list(map(int,input().split()))
    fun(ls)

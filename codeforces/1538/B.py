def fun(ls):
    st=sorted(ls)
    st=st[::-1]
    total=0
    count=0
    sm=sum(ls)
    if(sm%n!=0):
        print(-1)
        return 
    all_equal=True
    for i in st:
        if(i!=sm//n):
            all_equal=False
            break
    if(all_equal==True):
        print(0)
        return
    for i in st:
        if(i>sm//n):
            total+=i
            count+=1
        else:
            break
    print(count)



T = int(input())
# T=1
for i in range(T):
    n=int(input())
    # st=input()
    # ts=input()
    # ks= list(map(int, input().split()))    
    # ls= list(map(int, input().split()))    
    ls= list(map(int, input().split()))    
    fun(ls)
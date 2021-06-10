def fun(ls):
    mx=max(ls)
    mn=min(ls)
    mn_index=-1
    mx_index=-1
    for i , val in enumerate(ls):
        if(val==mn):
            mn_index=i
        if(val==mx):
            mx_index=i

    a=max(mn_index+1,mx_index+1)
    b=max(n-mn_index,n-mx_index)
    c=(mn_index+1+n-mx_index)
    d=(mx_index+1+n-mn_index)

    ans= min(a,b,c,d)
    print(ans)



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
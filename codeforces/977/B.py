def fun(n,st):
    ans=-1
    val=None
    for i in range(n-1):
        count=0
        current_two=st[i:i+2]
        for j in range(i+1,n-1):
            now=st[j:j+2]
            if(now==current_two):
                count+=1
        if(count>ans):
            ans=count
            val=current_two
    print(val)


    

# T = int(input())
T=1
for i in range(T):
    # var=input()
    n=int(input())
    st=input()
    # ks= list(map(int, input().split()))
    # ms= list(map(int, input().split()))
    # n=int(input())
    # ls= list(map(int, input().split()))
    fun(n,st)
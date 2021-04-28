def fun(ls,n):
    count_odd=0
    count_even=0
    st_odd=set()
    st_even=set()
    for i in ls:
        if(i%2!=0):
            count_odd+=1
            st_odd.add(i)
        else:
            count_even+=1
            st_even.add(i)
    if(count_odd%2==0 and count_even%2==0 or count_odd==n or count_even==n):
        print('YES')
    else:
        for i in st_odd:
            if(i+1 in st_even or i-1 in st_even):
                print('YES')
                return
        print('NO')
        



T = int(input())
ls=[]
for i in range(T):
    # var=input()
    # st=input()
    # val=int(input())
    # ks= list(map(int, input().split()))
    # ms= list(map(int, input().split()))
    val=int(input())
    ls= list(map(int, input().split()))
    fun(ls,val)
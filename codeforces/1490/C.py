def fun(ls):
    # like two sum
    n=ls[0]
    st=set()
    i=1
    ip3=1
    while(ip3<n):
        st.add(ip3)
        i+=1
        ip3=pow(i,3)
    for i in st:
        if(n-i in st):
            print('yes')
            return
    print('no')



    
T = int(input())
for i in range(T):
    # ls = list(map(int,input().split()))
    ls = list(map(int,input().split()))
    fun(ls)

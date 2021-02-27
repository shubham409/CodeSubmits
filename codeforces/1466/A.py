def fun(ls):
    st=set()
    for i in range(len(ls)):
        for j in range(i+1,len(ls)):
            st.add((abs(ls[i]-ls[j])/2))
    print(len(st))


    

    
T= int(input())
for i in range(T):
    t= int(input())
    # n= int(input())
    # m= int(input())
    ls= list(map(int,input().split()))
    fun(ls)
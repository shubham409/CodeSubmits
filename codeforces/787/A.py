def fun(ls, lt):
    a, b = ls
    c, d = lt
    st=set()
    for i in range(1,101):
        first= b + (i-1)*a
        st.add(first)

    for i in range(1,101):
        second= d + (i-1)*c
        if(second in st):
            print(second)
            return
    print(-1)

# T = int(input())
# for i in range(T):
    # t= int(input())
ls = list(map(int, input().split()))
lt = list(map(int, input().split()))
fun(ls, lt)
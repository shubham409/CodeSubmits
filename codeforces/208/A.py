def fun(st):
    st=st.replace('WUB' ,' ')
    print(*(st.split()))

T=1
for i in range(T):
    st=input()
    fun(st)
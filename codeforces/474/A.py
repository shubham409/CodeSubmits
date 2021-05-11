def fun(st,n):        
    s='qwertyuiopasdfghjkl;zxcvbnm,./'
    ans=''
    for i in st:
        ans+=s[s.find(i)+[1,-1][n=='R']]
    print(ans)

T=1
for i in range(T):
    n=input()
    st=input()
    fun(st,n)
def fun(st,n):        
    s='qwertyuiopasdfghjkl;zxcvbnm,./'
    ans=''
    for i in st:
        ans+=s[s.find(i)+[1,-1][n=='R']]
    print(ans)







    

# T = int(input())
T=1
for i in range(T):
    n=input()
    st=input()
    # val=int(input())
    # st=input()
    # ts=input()
    # ks= list(map(int, input().split()))    
    # ls= list(map(int, input().split()))    
    fun(st,n)
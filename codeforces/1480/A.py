
def fun(st):
    ans=''
    for i,val in enumerate(st):
        if(i%2==0):
            if val=='a':
                ans+='b'
            else:
                ans+='a'
        else:
            if val=='z':
                ans+='y'
            else:
                ans+='z'
    print(ans)



T= int(input())
for i in range(T):
    # t= int(input())
    # ls= list(map(int,input().split()))
    st= input()
    fun(st)
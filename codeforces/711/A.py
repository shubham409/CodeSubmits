import sys
def fun(st,n): 
    done=False
    ans=[]    
    for i in st:
        if( not done):
            if('OO' in i):
                ans.append(i.replace('OO','++',1))
                done=True
            else:
                ans.append(i)
        else:
            ans.append(i)
    if(done==False):
        print('NO')
    else:
        print('YES')
        for i in ans:
            print(i,end='')

T=1
for i in range(T):
    n=int(input())
    st=sys.stdin.readlines()
    fun(st,n)
def fun(n,st):
    if(st==('1'*n)):
        print('DRAW')
        return
    if(n==1 or n%2==0):
        print('BOB')
    else:
        count1=0
        count0=0
        for i in st:
            if(i=='1'):
                count1+=1
            else:
                count0+=1
        if(count0==1 and count1==n-1):
            print('BOB')
            return
        mid=(n//2)
        if(st[mid]=='1'):
            print('BOB')
        else:
            print('ALICE')
    
T=int(input())
for i in range(T):
    n=int(input())
    st=input()
    fun(n,st)
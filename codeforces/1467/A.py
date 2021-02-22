def fun(n):
    if(n==1):
        print(9)
        return
    if(n==2):
        print(98)
        return   
    if(n==3):
        print(989)
        return    
    st='989' 
    # i=9
    count=3
    # first=False
    # while(count<n):
    #     if(i==0):
    #         st+=str(i)
    #         i=1
    #         count+=1
    #         break
    #     else:
    #         st+=str(i)
    #         i-=1
    #         count+=1
    i=0
    while count<n:
        if(i==9):
            st+=str(i)
            i=0
            count+=1
        else:
            st+=str(i)
            i+=1
            count+=1
    print(st)
 
T= int(input())
for i in range(T):
    # t= int(input())
    # ls= list(map(int,input().split()))
    st= input()
    fun(int(st))
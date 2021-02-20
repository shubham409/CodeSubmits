from math import floor,ceil    
def fun(ls):
    # like two sum
    n=ls
    i=1
    ip3=1
    while(ip3<n):
        ans = pow(n-ip3,1/3)
        # ans=int(ans)

        if(pow(ceil(ans),3) ==n-ip3 or pow(floor(ans),3)==n-ip3):
            
            return 'yes'

        i+=1
        ip3=pow(i,3)
    return 'no'




dct={}
T = int(input())
for i in range(T):
    
    ls = int(input())
    if(dct.get(ls)!=None):
        print(dct.get(ls))
        continue

    ans = fun(ls)
    print(ans)
    dct[ls]=ans
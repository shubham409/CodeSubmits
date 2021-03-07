from collections import Counter
def fun(ls):
    dct=Counter(ls)
    st={4,7}
    if(dct.get(4)==None):
        if(dct.get(7) in st):
            print('YES')
            return
        else:
            print('NO')
            return
    
    if(dct.get(7)==None):
        if(dct.get(4) in st):
            print('YES')
            return
        else:
            print('NO')
            return

    if(dct.get(4)!=None and dct.get(7)!=None):
        if( dct.get(4)+dct.get(7)  in st ):
            print('YES')
            return
        else:
            print('NO') 
            return   
        

# T = int(input())
# for i in range(T):
# n = list(map(int, input().split()))
# n = int(input())
ls = list(map(int, list(input())))
fun(ls)
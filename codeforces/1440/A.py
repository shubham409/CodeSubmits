from collections import Counter
def fun(n,c0,c1,h,st):
    dct=Counter(st)
    # h for each charecter change
    # c0 for buying 0
    # c1 for buying 1
    count1= dct.get('1') if dct.get('1')!=None else 0
    count0= dct.get('0') if dct.get('0')!=None else 0
    if(c0>c1):
            print(min(((count1+count0)*c1 + count0*h),(count1*c1+count0*c0)))
    else:
            print(min(((count1+count0)*c0 + count1*h),(count1*c1+count0*c0)))


    

T= int(input())
for i in range(T):
    # t= int(input())
    n,c0,c1,h= list(map(int,input().split()))
    st=input()
    fun(n,c0,c1,h,st)
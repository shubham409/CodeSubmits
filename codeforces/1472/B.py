from collections import Counter
def fun(ls):
    dct = Counter(ls)
    if(dct.get(1)==None):
        dct[1]=0
    if(dct.get(2)==None):
        dct[2]=0
    one=dct.get(1)
    two=dct.get(2)
    value_of_two=2*two
    value_of_one=1*one
    if((value_of_one+value_of_two)%2==0):
        if(one==0 and two%2!=0):
            print('no')
            return
        print('yes')
    else:
        print('no')


T= int(input())
for i in range(T):
    t= int(input())
    ls= list(map(int,input().split()))
    fun(ls)
from collections import Counter

def fun(st):
    first=st[0]
    last= st[-1]
    if(len(st)%2!=0):
        print('no')
        return
    if(first==last):
        print('no')
        return
    dct= Counter(st)
    if(dct.get(first)>dct.get(last)):
        mid=')'
    else:
        mid='('
    new_str=''
    for i in st:
        if (i==first):
            new_str+='('
            continue
        if(i==last):
            new_str+=')'
            continue
        new_str+=mid
    ob=0
    # cb=0
    # print(new_str)
    for i in new_str:
        if(i=='('):
            ob+=1
            # continue
        if(i==')'):
            ob-=1
            # continue
        if(ob<0):
            print('no')
            return
    if(ob!=0):
        print('no')
        return 
    print('yes')






     


T= int(input())
for i in range(T):
    # ls= list(map(int,input().split()))
    st= input()
    fun(st)

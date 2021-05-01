def fun(ls):
    chris=0
    mishka=0
    m='Mishka'
    c='Chris'
    d='Friendship is magic!^^'
    for i in ls:
        if(i[0]>i[1]):
            mishka+=1
        if(i[0]<i[1]):
            chris+=1
    if(chris>mishka):
        print(c)
    if(mishka>chris):
        print(m)
    if(mishka==chris):
        print(d)

    


    

T = int(input())
ls=[]
for i in range(T):
    # var=input()
    # st=input()
    # val=int(input())
    # ks= list(map(int, input().split()))
    # ms= list(map(int, input().split()))
    # n=int(input())
    # ls= list(map(int, input().split()))
    ls.append(list(map(int, input().split())))
fun(ls)
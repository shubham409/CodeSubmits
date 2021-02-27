def fun(r,b):
    rl = len(r)
    bl = len(b)
    pr=0
    pb=0
    # if(sum(r)>sum(b)):
    #     print('RED')
    # if(sum(r)<sum(b)):
    #     print('BLUE')
    # if(sum(r)==sum(b)):
    #     print('EQUAL')
    for i in range(rl):
        # for j in range(bl):
            # print(r[i],b[j])
        j=i
        if(r[i]>b[j]):
            pr+=1
        if(b[j]>r[i]):
            pb+=1
        if(r[i]==b[j]):
            pr+=0
            pb+=0


    if(pr==pb):
        print('EQUAL')
    if(pr>pb):
        print('RED')    
    if(pr<pb):
        print('BLUE')
T= int(input())

for i in range(T):
    t=input()
    r= input()
    r= list(map(int,list(r)))
    b= input()
    b= list(map(int,list(b)))    
    # st= input()
    # t= input()
    # fun(st)
    fun(r,b)
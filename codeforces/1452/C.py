def fun(st):
    ob='('
    cb=')'
    osb='['
    csb=']'
    ls=[]
    count=0
    count_ob=0
    count_sob=0
    for i in st:
        # print(i)
        if (i==ob or i==osb):
            if (i==ob):
                count_ob+=1
            else:
                count_sob+=1
        else:
            if(i==cb):
                if (count_ob>0):
                    count_ob-=1
                    count+=1
            if(i==csb):
                if (count_sob>0):
                    count_sob-=1
                    count+=1
    print(count)

T= int(input())
for i in range(T):
    t= input()
    fun(t)    
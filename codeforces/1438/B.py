def fun(ls):
    # concept
    # if we have to get 2^n from number of 2^m then at least one number must repeat
    #  i.e you cant get any 2^n from all distict 2^m
    if(len(set(ls))<len(ls)):
        print('yes')
    else:
        print('no')
T= int(input())
for i in range(T):
    t= int(input())
    ls= list(map(int,input().split()))
    fun(ls)
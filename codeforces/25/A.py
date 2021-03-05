def fun(ls):
    odd=0
    even=0
    position_odd=0
    position_even=0
    position=0
    for i in ls:
        position+=1
        if(i%2==0):
            even+=1
            position_even=position
        else:
            odd+=1
            position_odd=position
    if(odd>even):
        print(position_even)
    else:
        print(position_odd)

# T = int(input())
# for i in range(T-1):
T = int(input())
ls = list(map(int, input().split()))
fun(ls)
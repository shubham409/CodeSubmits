def fun(n):
    lamak,bob=n
    count=0
    while lamak<=bob:
        lamak*=3
        bob*=2
        count+=1
    print(count)        


    
        

# T = int(input())
# for i in range(T):
# n = list(map(int, input().split()))
# n = int(input())
ls = list(map(int, input().split()))
fun(ls)




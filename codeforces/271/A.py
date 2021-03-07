def fun(n):
    n=n+1
    length=len(set(list(str(n))))
    while(length!=4):
        n+=1
        length=len(set(list(str(n))))
    print(n)


    
        

# T = int(input())
# for i in range(T):
# n = list(map(int, input().split()))
n = int(input())
# ls = list(map(int, input().split()))
fun(n)










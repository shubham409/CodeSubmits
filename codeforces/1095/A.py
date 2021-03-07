def fun(st):
    n=0
    i=0
    ans=''
    length= len(st)
    while n<length:
        n=n+i
        if(n<length):
            ans+=st[n]
        i+=1
    print(ans)

      
        

# T = int(input())
# for i in range(T):
# n = list(map(int, input().split()))
n = int(input())
# ls = list(map(int, list(input())))
ipt= input()
fun(ipt)

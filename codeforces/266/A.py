def fun(st):
    prv=None
    count=0
    for i in st:
        
        if(prv==i):
            count+=1
        else:
            prv=i
    print(count)


 
    

# T= int(input())
# for i in range(T):
t= int(input())
# ls= list(map(int,input().split()))
st=input()
fun(st)
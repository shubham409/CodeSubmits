def fun(ls,n):
    count=0
    ans=[]
    number_of_elements=0
    for ind,i in enumerate(ls):
        number_of_elements+=1
        if(i<0):
            count+=1
        if(count>2):
            ans.append(number_of_elements-1)
            count=1
            number_of_elements=1

        if(ind==n-1):
            ans.append(number_of_elements)
            count=0
    print(len(ans))
    print(*ans)



# T = int(input())
# for i in range(T):
n = int(input())
ls=list(map(int,input().split()))
fun(ls,n)
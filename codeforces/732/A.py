a,b=map(int,input().split())
i=1
while a*i%10!=b and a*i%10!=0:
    i+=1
print(i)
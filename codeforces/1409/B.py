for i in range(int(input())):
    a,b,x,y,n=map(int,input().split())
    c=(a-min(a-x,n))*(b-min(b-y,n-min(a-x,n)))
    z=(b-min(b-y,n))*(a-min(a-x,n-min(b-y,n)))
    print(min(c,z))
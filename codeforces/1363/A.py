for _ in range(int(input())):
    n,x=map(int,input().split())
    ar=[int(x) for x in input().split()]
    l=[i%2 for i in ar]
    c=l.count(True)
    if(c==0 or (c==n and x%2==0) or (c%2==0 and n==x)):
	    print("NO")
    else:
        print("YES")
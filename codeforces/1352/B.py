for i in range(int(input())):
    n,k = map(int,input().split())
    if n % 2 == 0 and n >= 2*k:
    	print("YES")
    	print("2 " * (k-1), n - 2*(k-1))
    elif n - k >=0 and (n-k+1)% 2 !=0:
    	print("YES")
    	print("1 " * (k-1),n-k+1)	
    else:
    	print("NO")
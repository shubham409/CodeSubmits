for _ in range(int(input())):
	n=int(input())
	if(n==1 or n==2 or n==4):print(-1)
	elif(n%3==0):print(n//3,0,0)
	elif((n-5)%3==0):print((n-5)//3,1,0)
	else:print((n-7)//3,0,1)
a=int(input())
for i in range (0,a): 
	n,m=map(int,input().split())
	c=0
	for i in range(0,n): 
		l=input()
		if l[m-1]=='R': 
			c+=1
	c+=l.count('D')
	print(c)
for i in range(int(input())):
	a,b,c,d=map(int,input().split())
	print(max(c-1,a-c)+max(d-1,b-d))
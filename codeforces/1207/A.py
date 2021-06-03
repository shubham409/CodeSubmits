t=int(input())
for i in range(t):
	b,p,f=map(int,input().split())
	h,c=map(int,input().split())
	ans=0
	for i in range(min(p,b//2)+1):
		r=b-2*i
		ans=max(ans,i*h+min(r//2,f)*c)
	print(ans)

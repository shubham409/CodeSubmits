m=int(input())
for i in range(m):
	n,k=map(int,input().split())
	a=list(map(int,input().split()))
	b=list(map(int,input().split()))
	a.sort()
	b.sort(reverse=True)
	for j in range(k):
		if(a[j]<b[j]):
			a[j]=b[j]
	print(sum(a))

def fun(st):
	count=0
	for i in st:
		if i=='Q':
			count= count+1
	ans=0
	leftq=0
	rightq=count
	for i in st:
		if i=='Q':
			leftq+=1
			rightq-=1
		if i=='A':
			ans+=leftq*rightq
	print(ans)



st=  input()
fun(st)

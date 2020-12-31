def fun(num):
	ls=[]
	for i in range(num):
		if i==0:
			ls.append(1)
			continue
		else:
			ls.append(4*i+ls[i-1])
	print(ls[-1])

	

# ipt=input()
ls= list(map(int, input().split()))
fun(ls[0])

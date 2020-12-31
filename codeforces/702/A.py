def fun(ls):
	ar=[0]*len(ls)
	for i,val in enumerate(ls):
		if i ==0:
			ar[i]=1
			continue
		else:
			if ls[i-1]<val:
				ar[i]=ar[i-1]+1
			else:
				ar[i]=1
	print(max(ar))

ipt=input()
ls= list(map(int, input().split()))
fun(ls)
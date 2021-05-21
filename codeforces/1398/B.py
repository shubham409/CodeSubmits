for t in range(int(input())):
	a = map(len,input().split('0'))
	print(sum(sorted(a,reverse=True)[0::2]))

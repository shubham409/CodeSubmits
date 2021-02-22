

def fun(ls,num):
	count=0
	set1= set()
	for i in range(num):
		if ls[i] in set1:
			if ls[i]+1 in set1:
				continue
			else:
				set1.add(ls[i]+1)
				count+=1
		else:
			set1.add(ls[i])
			count+=1
	print(count)
 
 
ipt= int(input())
for i in range(ipt):
	num= int(input())
	ls= input().split()
	ls= list(map(int,ls))
	fun(ls,num)
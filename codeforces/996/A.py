def fun(num):
	ans=0
	val=100
	if num>=val:
		ans+=int (num/val)
		num =num%val
	val=20
	if num>=val:
		ans+=int (num/val)
		num =num%val
	val=10
	if num>=val:
		ans+=int (num/val)
		num =num%val
	val=5	
	if num>=val:
		ans+=int (num/val)
		num =num%val
	val=1	
	if num>=val:
		ans+=int (num/val)
		num =num%val
	print(ans)
# ipt=input()
ls= list(map(int, input().split()))
fun(ls[0])
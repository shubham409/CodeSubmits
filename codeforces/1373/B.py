for _ in range(int(input())):
	s=input()
	one=s.count('1')
	zero=s.count('0')
	p=min(one,zero)
	if(p%2)==1:
		print('DA')
	else:
		print('NET')
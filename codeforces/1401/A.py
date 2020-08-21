def fun(ls):
     n = ls[0]
     k = ls[1]
     # AB - OB
     if n%2!=0  and k%2==0 and k <n:
     	print(1)
     	return
     if n%2==0  and k%2!=0 and k <n:
     	print(1)
     	return     	
     if k <= n  :
     	print(0)
     if k> n:
     	print(k-n)


     
T = int(input())
for i in range (T):
     x = input ().split()
     x= list(map(int , x))

     fun(x)
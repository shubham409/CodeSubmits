k,l,m,n,d = (int(input()) for i in range(5))
print(sum(1-all((i%k,i%l,i%m,i%n))for i in range(1,d+1)))
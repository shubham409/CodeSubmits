n,m,k=map(int,input().split())
x=[int(input()) for t in range(m+1)]
print(sum(bin(x[m]^y).count('1')<=k for y in x)-1)
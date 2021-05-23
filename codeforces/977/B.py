n=int(input())
a=input()
k=[a[i:i+2] for i in range(n-1)]
print(max(k,key=k.count))
a='qwertyuiopasdfghjkl;zxcvbnm,./'
n=input()
for i in input():
    print(a[a.index(i)+[1,-1][n=="R"]],end='')
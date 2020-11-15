def fun(num):
    ls = [1 for i in range(num)]
    print(*ls)

var = input()
for _ in range(int(var)):
    num = input()
    num= int(num)
    fun(num)
def fun(ls, lt):
    st = set(ls)
    count = 0
    for i in lt:
        if(i in st):
            count += 1
    print(count)


T = int(input())
for i in range(T):
    n, k = list(map(int, input().split()))
    ls = list(map(int, input().split()))
    lt = list(map(int, input().split()))
    fun(ls, lt)
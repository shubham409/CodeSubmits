from math import ceil


def fun(ls, n, k):
    # approach ->
    # we must waste some greater elements but
    # we can always choose smaller elements before the median
    median_position = ceil(n / 2)
    median_index = median_position - 1
    waste_elements = n - median_position
    ans = 0
    count = 0
    number_of_mediums = 0
    for i in ls[-1::-1]:
        count += 1
        if(number_of_mediums >= k):
            break
        if(count > waste_elements):
            ans += i
            count = 0
            number_of_mediums += 1
    print(ans)


T = int(input())
for i in range(T):
    n, k = list(map(int, input().split()))
    ls = list(map(int, input().split()))
    fun(ls, n, k)
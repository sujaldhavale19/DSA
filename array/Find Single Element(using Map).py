def single_element(arr,n):
    m = {}
    for num in arr:
        if num in m:
            m[num] += 1
        else:
            m[num] = 1
    for key, value in m.items():
        if value == 1:
            return key

    return -1
n = int(input())
arr = list(map(int, input().split()))
result = single_element(arr,n)
print(result)

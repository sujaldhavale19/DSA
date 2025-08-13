def remove_duplicates(a, n):
    i = 0
    for j in range(1, n):
        if a[i] != a[j]:
            a[i + 1] = a[j]
            i += 1
    return i + 1

if __name__ == "__main__":
    n = int(input())
    a = list(map(int, input().split()))
    unique_count = remove_duplicates(a, n)
    print(unique_count)
    for i in range(n):
        print(a[i], end=" ")

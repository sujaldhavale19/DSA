def move_zeros(a, n):
    i = 0
    for j in range(n):
        if a[j] != 0:
            a[i], a[j] = a[j], a[i]
            i += 1

if __name__ == "__main__":
    n = int(input())
    a = list(map(int, input().split()))
    move_zeros(a, n)
    for i in range(n):
        print(a[i], end=" ")

t = int(input())
for i in range(t):
    n = int(input())
    a = list(map(str, input().split()))
    m = n
    if n == 1:
        print(1)
        continue
    elif n == 2:
        if a[0] == a[1]:
            print(1)
            continue
    else:
        for i in range(1, n):
            if a[i] == a[i - 1]:
                m -= 1
    print(m)
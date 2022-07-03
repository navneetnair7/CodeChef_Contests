t = int(input())
for i in range(t):
    n, m, k = map(int, input().split())
    a = list(map(int, input().split()))
    l = [0] * 1000
    for i in range(n):
        l[a[i]] += 1
    for i in range(m):
        if l[k] == 0:
            print("YES")
            break
        else:
            print("NO")
            break
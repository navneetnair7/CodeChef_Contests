t = int(input())
for i in range(t):
    n, x, y = map(int, input().split())
    if 1 * x + 2 * y <= n:
        print("YES")
    else:
        print("NO")
t = int(input())
for i in range(t):
    a, b = map(int, input().split())
    s = b - a
    if s % 3 == 2:
        print("NO")
    else:
        print("YES")
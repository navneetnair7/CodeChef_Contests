t = int(input())
for i in range(t):
    x, y = map(int, input().split())
    print(abs((x  - 1) // 10 - (y - 1) // 10))
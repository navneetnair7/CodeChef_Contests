t = int(input())
for i in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    if n % 2 != 0:
        print(-1)
    else:
        print(abs(a.count(1) - a.count(-1)) // 2)
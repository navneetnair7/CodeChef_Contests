t = int(input())
for i in range(t):
    n = int(input())
    b = list(map(int, input().split()))
    a = []
    s = sum(b) // (n + 1)
    for i in range(n):
        print(b[i] - s, end = ' ')
    print()
t = int(input())
for i in range(t):
    x, y, a = map(int, input().split())
    print("YES" if a < y and a >= x else "NO")
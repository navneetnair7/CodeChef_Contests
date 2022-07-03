t = int(input())
for i in range(t):
    x, y = map(int, input().split())
    print(x if x > y else y)
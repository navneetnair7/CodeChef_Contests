t = int(input())
for i in range(t):
    x, y, z = map(int, input().split())
    if x / y > 1 and x % y != 0:
        print((x // y + 1) * z)
    elif x / y > 1 and x % y == 0:
        print((x // y) * z)
    else:
        print(z)
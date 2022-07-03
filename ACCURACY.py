t = int(input())
for i in range(t):
    x = int(input())
    if x % 3 == 0:
        print("0")
    else:
        print((x // 3 + 1) * 3 - x)
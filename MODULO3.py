t = int(input())
for i in range(t):
    a, b = map(int, input().split())
    count = 0
    a1 = a // 3
    a2 = a % 3
    b1 = b // 3
    b2 = b % 3
    if a == 0 or b == 0 or a2 == 0 or b2 == 0:
        print(0)
        continue
    if a2 == b2 or a == b:
        print(1)
    else:
        print(2)
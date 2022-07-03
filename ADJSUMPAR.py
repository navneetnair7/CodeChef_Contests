t = int(input())
for i in range(t):
    n = int(input())
    b = list(map(int, input().split()))
    a = []
    if n == 2:
        if (b[0] == 1 and  b[1] == 1) or (b[0] == 0 and b[1] == 0):
            print("Yes")
        else:
            print("No")
    else:
        if b.count(1) % 2 == 0:
            print("Yes")
        else:
            print("No")
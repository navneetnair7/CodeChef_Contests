t = int(input())
for i in range(t):
    n, k = map(int, input().split())
    if n % 2 == 0:
        print("Yes")
    else:
        if k % 2 == 0:
            print("No")
        else:
            print("Yes")
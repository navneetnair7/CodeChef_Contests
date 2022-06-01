t = int(input())
for i in range(t):
    l = list(map(int, input().split()))
    if max(l[:2]) > max(l[2:]):
        print("Q")
    elif max(l[:2]) < max(l[2:]):
        print("P")
    else:
        print("TIE")
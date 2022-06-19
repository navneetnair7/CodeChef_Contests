t = int(input())
for i in range(t):
    p, q = map(int, input().split())
    print("Alice" if (p + q) % 4 == 0 or (p + q -1) % 4 == 0 else "Bob")
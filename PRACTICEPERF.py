p = list(map(int, input().split()))
count = 0
for i in p:
    count += 1 if i >= 10 else 0 
print(count)
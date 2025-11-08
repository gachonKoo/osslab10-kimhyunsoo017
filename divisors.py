n = int(input().strip())

ans = []
for i in range(1, n + 1):
    if n % i == 0:
        ans.append(str(i))

print(' '.join(ans))

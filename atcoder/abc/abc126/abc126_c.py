N, K = map(int, input().split())

ans = 0

for n in range(1, N+1):
    if n >= K:
        ans += 1.0
    else:
        tmp  = 1.0
        while n < K:
            tmp /= 2
            n   *= 2
        ans += tmp

ans /= N

print(ans)

import bisect


N, M = map(int, input().split())

S = {int(input()) for _ in range(N)}
S = S | {0}

# list of score, 2 throw
L = sorted(list({x + y for x in S for y in S if x + y <= M}))

ans = 0

for l in L:
    tmp = L[bisect.bisect_right(L, M - l) - 1]
    ans = max(ans, l + tmp)

print(ans)

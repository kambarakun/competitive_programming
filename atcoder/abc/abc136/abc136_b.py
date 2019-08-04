N = int(input())
L = len(str(N))

ans = 0

for l in range(1, L, 2):
    if l != L:
        ans += 9 * 10 ** (l-1)

if L % 2 == 1:
    ans += N - (10 ** (L-1) - 1)

print(ans)

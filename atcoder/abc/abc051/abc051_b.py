K, S = map(int, input().split())

R = 0

for X in range(max(0, S-2*K), K+1):
    for Y in range(max(0, S-X-K), K+1):
        if X + Y <= S:
            R += 1

print(R)

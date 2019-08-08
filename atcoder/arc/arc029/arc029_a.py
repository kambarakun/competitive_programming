import itertools


N = int(input())
T = [int(input()) for _ in range(N)]

R = sum(T)

for pattern in itertools.product([False, True], repeat=N):
    A = [t for i, t in enumerate(T) if pattern[i]]
    B = [t for i, t in enumerate(T) if pattern[i] == False]
    R = min(R, max(sum(A), sum(B)))

print(R)

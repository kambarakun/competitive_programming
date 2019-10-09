N = int(input())
V = list(map(int, input().split()))
C = list(map(int, input().split()))

D = [V[n] - C[n] for n in range(N)]
D = [d for d in D if d > 0]

print(sum(D))

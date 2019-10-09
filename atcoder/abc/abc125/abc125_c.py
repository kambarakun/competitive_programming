from fractions import gcd


N = int(input())
A = list(map(int, input().split()))

G_FW    = [None] * N
G_FW[0] = A[0]

for i in range(1, N):
    G_FW[i] = gcd(G_FW[i-1], A[i])

G_RV     = [None] * N
G_RV[-1] = A[-1]

for i in reversed(range(0, N-1)):
    G_RV[i] = gcd(G_RV[i+1], A[i])

G     = [None] * N
G[ 0] = G_RV[1]
G[-1] = G_FW[-2]

for i in range(1, N-1):
    G[i] = gcd(G_FW[i-1], G_RV[i+1])

print(max(G))

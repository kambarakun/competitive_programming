import numpy as np


N, H = map(int, input().split())

A = [None] * N
B = [None] * N

for n in range(N):
    A[n], B[n] = map(int, input().split())

A = sorted(A, reverse=True)
B = sorted(B, reverse=True)

S = np.cumsum(B)
try:
    S = S[:int(np.where(S >= H)[0])+1]
except:
    pass

result = H

for i, s in enumerate(S):
    result = min(result, i + 1 + int(np.ceil(max(0, H - S[i]) / A[0])))

print(result)

N, A, B = map(int, input().split())

X = list(map(int, input().split()))
X = [x - X[0] for x in X]

C = 0

for i in range(1, N):
    C_A = (X[i] - X[i-1]) * A
    if C_A < B:
        C += C_A
    else:
        C += B

print(C)

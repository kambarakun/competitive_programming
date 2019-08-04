N = int(input())

X = [None] * N
Y = [None] * N

for n in range(N):
    x, y = map(int, input().split())
    X[n] = x
    Y[n] = y

L = {(X[i] - X[j]) ** 2 + (Y[i] - Y[j]) ** 2  for i in range(N) for j in range(N) if i != j}

print(max(L) ** 0.5)

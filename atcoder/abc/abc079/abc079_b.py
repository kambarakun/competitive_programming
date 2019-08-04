L = [0] * 87

for n, l in enumerate(L):
    if n == 0:
        L[0] = 2
    elif n == 1:
        L[1] = 1
    else:
        L[n] = L[n-1] + L[n-2]

N = int(input())

print(L[N])

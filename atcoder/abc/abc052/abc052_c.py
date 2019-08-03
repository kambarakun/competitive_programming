def get_prime_factorized(N):
    R = []
    b, e = 2, 0
    while b ** 2 <= N:
        while N % b == 0:
            N  = N // b
            e += 1
        if e > 0:
            R.append([b, e])
        b, e = b + 1, 0
    if N > 1:
        R.append([N, 1])
    return R


N = int(input())
H = {}
R = 1

for n in range(1, N+1):
    for l in get_prime_factorized(n):
        k, c = l
        if k in H.keys():
            H[k] += c
        else:
            H[k]  = c

for k in H.keys():
    R *= (H[k]+1)
    R %= 10**9+7

print(R)

A = int(input())
B = int(input())
C = int(input())
D = int(input())
E = int(input())

L = [A, B, C, D, E]
M = [l // 10 * 10 if l % 10 == 0 else (l // 10 + 1) * 10 for l in L]
N = [l % 10 for l in L]
N = [n if n != 0 else 10 for n in N]

zipped  = zip(L, M, N)
zipped  = sorted(zipped, key=lambda x: [x[2]], reverse=False)
L, M, N = map(list, zip(*zipped))

print(L[0] + sum(M[1:]))

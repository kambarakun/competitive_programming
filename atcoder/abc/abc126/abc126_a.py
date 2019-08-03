N, K   = map(int, input().split())
S      = input()

print(S[:K-1] + str.lower(S[K-1]) + S[K:])

N, K = map(int, input().split())
S    = input()

L = S.replace('01', '0,1')
L = L.replace('10', '1,0')
L = L.split(',')
L = [len(l) for l in L]

if S[0] == '0':
    L = [0] + L

R = []
for i in range(max(1, len(L) // 2 + 1 - K)):
    if i == 0:
        R.append(sum(L[2*i:2*(i+K)+1]))
    else:
        R.append(R[-1] - sum(L[2*(i-1):2*(i-1)+2]) + sum(L[2*(i+K)-1:2*(i+K)+1]))

print(max(R))

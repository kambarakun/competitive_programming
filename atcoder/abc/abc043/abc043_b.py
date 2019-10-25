S = list(input())

R = ''

for s in S:
    if s == 'B':
        R = R[:-1]
    else:
        R = R + s

print(R)

N = int(input())
S = input()
R = [None] * N

for i, s in enumerate(S):
    if i == 0:
        if s == 'I':
            R[i] =  1
        else:
            R[i] = -1
    else:
        if s == 'I':
            R[i] = R[i-1] + 1
        else:
            R[i] = R[i-1] - 1

print(max(0, max(R)))

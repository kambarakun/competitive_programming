S = input()
N = len(S)
A = [0] * N

step_R  = [0] * N
count_R = 1
step_L  = [0] * N
count_L = 1

for i in range(1, N):
    if S[i-1] == 'R':
        if S[i] == 'L':
            for j in range(count_R):
                step_R[i-1-j] = j+1
            count_R  = 1
        else:
            count_R += 1

for i in range(1, N)[::-1]:
    if S[i] == 'L':
        if S[i-1] == 'R':
            for j in range(count_L):
                step_L[i+j] = j+1
            count_L  = 1
        else:
            count_L += 1

steps = [max(step_R[i], step_L[i]) for i in range(N)]

for i in range(N):
    step = steps[i]
    if S[i] == 'R':
        if step % 2 == 0:
            A[i+step]   += 1
        else:
            A[i+step-1] += 1
    else:
        if step % 2 == 0:
            A[i-step]   += 1
        else:
            A[i-step+1] += 1

print(' '.join([str(a) for a in A]))

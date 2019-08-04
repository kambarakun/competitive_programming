N, Y = map(int, input().split())

is_fail = True

for a in range(N+1):
    for b in range(N+1-a):
        if Y - 10000 * a - 5000 * b == 1000 * (N - a - b):
            print(a, b, N - a - b)
            is_fail = False
            break
    if not is_fail:
        break

if is_fail:
    print('-1 -1 -1')

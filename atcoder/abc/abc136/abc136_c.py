N = int(input())
H = list(map(int, input().split()))

is_fail = False

for i in list(range(1, N))[::-1]:
    if H[i-1] <= H[i]:
        continue
    elif H[i-1] == H[i] + 1:
        H[i-1]  -= 1
    if H[i-1] > H[i]:
        is_fail = True
        break

if not is_fail:
    print('Yes')
else:
    print('No')

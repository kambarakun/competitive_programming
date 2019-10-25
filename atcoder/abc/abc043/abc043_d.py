S = list(input())

is_done_2 = False
is_done_3 = False

for i in range(len(S)-1):
    if len(set(S[i:i+2])) < 2:
        is_done_2 = True
        break

if not is_done_2:
    for j in range(len(S)-2):
        if len(set(S[j:j+3])) < 3:
            is_done_3 = True
            break

if is_done_2:
    print(i+1, i+2)
elif is_done_3:
    print(j+1, j+3)
else:
    print(-1, -1)

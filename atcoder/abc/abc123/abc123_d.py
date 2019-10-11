X, Y, Z, K  = map(int, input().split())

A = sorted(list(map(int, input().split())), reverse=True)[:K]
B = sorted(list(map(int, input().split())), reverse=True)[:K]
C = sorted(list(map(int, input().split())), reverse=True)[:K]

R  = [sum([A[0], B[0], C[0]])]
Q  = {(0, 0, 1), (0, 1, 0), (1, 0, 0)}
D  = {(0, 0, 0), (0, 0, 1), (0, 1, 0), (1, 0, 0)}
iS = [((a, b, c), sum([A[a], B[b], C[c]])) for a, b, c in Q if (a < X) and (b < Y) and (c < Z)]
iS = sorted(iS, key=lambda x: [x[1], x[0]], reverse=True)

while len(R) < K:
    R.append(iS[0][1])
    abc     = iS[0][0]
    a, b, c = abc[0], abc[1], abc[2]
    iS      = iS[1:]
    if a + 1 < X:
        if not (a + 1, b, c) in D:
            s = sum([A[a + 1], B[b], C[c]])
            is_done = False
            for i in range(len(iS)):
                if iS[i][1] < s:
                    iS = iS[:i] + [((a + 1, b, c), s)] + iS[i:]
                    is_done = True
                    break
            if is_done == False:
                iS = iS + [((a + 1, b, c), s)]
            D.add((a + 1, b, c))
    if b + 1 < Y:
        if not (a, b + 1, c) in D:
            s = sum([A[a], B[b + 1], C[c]])
            is_done = False
            for i in range(len(iS)):
                if iS[i][1] < s:
                    iS = iS[:i] + [((a, b + 1, c), s)] + iS[i:]
                    is_done = True
                    break
            if is_done == False:
                iS = iS + [((a, b + 1, c), s)]
            D.add((a, b + 1, c))
    if c + 1 < Z:
        if not (a, b, c + 1) in D:
            s = sum([A[a], B[b], C[c + 1]])
            is_done = False
            for i in range(len(iS)):
                if iS[i][1] < s:
                    iS = iS[:i] + [((a, b, c + 1), s)] + iS[i:]
                    is_done = True
                    break
            if is_done == False:
                iS = iS + [((a, b, c + 1), s)]
            D.add((a, b, c + 1))

for r in R:
    print(r)

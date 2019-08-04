import itertools


N, M  = map(int, input().split())
known = [[False for y in range(N)] for x in range(N)] # known[x][y]

for m in range(M):
    X, Y = map(int, input().split())
    known[X-1][Y-1] = True
    known[Y-1][X-1] = True

for pattern in itertools.product([False, True], repeat=N):
    query = [idx for idx, flag in enumerate(pattern) if flag]
    query

for result in range(N+1)[::-1]:
    if result == 1:
        break
    else:
        is_break = False
        for query in list(itertools.combinations(range(N), result)):
            if {known[i][j] for i in query for j in query if i != j} == set([True]):
                is_break = True
                break
        if is_break:
            break

print(result)

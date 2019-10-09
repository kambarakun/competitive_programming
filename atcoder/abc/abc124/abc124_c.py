S = list(map(int, list(input())))

R_0 = [s for i, s in enumerate(S) if s != (i % 2)]
R_1 = [s for i, s in enumerate(S) if s == (i % 2)]

print(min(len(R_0), len(R_1)))

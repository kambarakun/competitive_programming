N = int(input())
A = int(input())
B = int(input())
C = int(input())
D = int(input())
E = int(input())

R = min(A, B, C, D, E)

if N % R == 0:
    print(4 + N // R)
else:
    print(5 + N // R)

N = int(input())
A = list(map(int, input().split()))

K = len([a for a in A if a < 0])
B = sorted([abs(a) for a in A])

if K % 2 == 0:
    print(sum(B))
else:
    print(sum(B[1:]) - B[0])

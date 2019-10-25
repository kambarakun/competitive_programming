N = int(input())
A = list(map(int, input().split()))

print(min([sum([(a - x) ** 2 for a in A]) for x in range(-100, 100+1)]))

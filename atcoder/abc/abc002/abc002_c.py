xa, ya, xb, yb, xc, yc  = map(int, input().split())

print(abs((xb - xa) * (yc - ya) - (yb - ya) * (xc - xa)) / 2)

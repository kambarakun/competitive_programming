A, B, C, D = map(int, list(input()))

f = True

for op1 in range(2):
    for op2 in range(2):
        for op3 in range(2):
            if f == True:
                R = 0
                r = ''
                if op1 == 0:
                    R = A + B
                    r = '%s+%s' % (A, B)
                else:
                    R = A - B
                    r = '%s-%s' % (A, B)
                if op2 == 0:
                    R += C
                    r = '%s+%s' % (r, C)
                else:
                    R -= C
                    r = '%s-%s' % (r, C)
                if op3 == 0:
                    R += D
                    r = '%s+%s' % (r, D)
                else:
                    R -= D
                    r = '%s-%s' % (r, D)
                if R == 7:
                    print('%s=7' % r)
                    f = False

S  = input()
MM = ['%02i' % mm for mm in range(1, 12+1)]

if S[:2] in MM:
    if S[2:] in MM:
        print('AMBIGUOUS')
    else:
        print('MMYY')
else:
    if S[2:] in MM:
        print('YYMM')
    else:
        print('NA')

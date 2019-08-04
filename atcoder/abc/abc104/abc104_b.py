S = input()

if S[0] == 'A' and S[2:-1].count('C') == 1 and S.count('A') == 1 and S.count('C') == 1 and sum([s == s.upper() for s in S]) == 2:
    print('AC')
else:
    print('WA')

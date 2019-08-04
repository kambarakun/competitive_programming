S = input()

L = [S]

for i in range(len(S)-1):
    L_new = []
    for l in L:
        L_new.append(l[:1+2*i] + '+' + l[1+2*i:])
        L_new.append(l[:1+2*i] + ' ' + l[1+2*i:])
    L = L_new

print(sum([eval(str.replace(l, ' ', '')) for l in L]))

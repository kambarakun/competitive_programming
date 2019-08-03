#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# 整数入力
N = int(input())


# 複数整数
A, B = map(int, input().split())


# 整数リスト（1行）
L = list(map(int, input().split()))


# 整数リスト（N行）
L = [int(input()) for _ in range(N)]


# 複数整数 + 整数リスト（手入力では動作完了しない）
N, K, *L = map(int, open(0).read().split())


# 生文字列
S = input()


# 文字列分解（"ABC" -> ['A', 'B', 'C']）
S = list(input())


# 複数文字列（"ABC DE"）
s1, s2 = input().split()


# 混合（整数と文字列）を取り敢えず文字列で読み取る
A, op, B = input().split()


# リストのユニーク化（順序は破壊される）
L = ['a', 'a', 'b']
L = list(set(L))


# リストの和集合・積集合
a = [2, 4, 6, 8]
b = [3, 6, 9]

print(list(set(a) | set(b)))  # 和集合 [2, 3, 4, 6, 8, 9]
print(list(set(a) & set(b)))  # 積集合 [6]


# リストの reverse
A = [1, 2, 3]
B = A[::-1]


# 典型マトリックス（○×とか文字列）
H, W = map(int, input().split())
M    = [None] * H # print(M[h][w])
for h in range(H):
    M[h] = list(input())


# 固定長リスト最速初期化
L = [None] * N
M = [[None for y in range(N)] for x in range(N)]


# 複数のリストを連動させてソート（reverse=True）, 多重ソート
a = [1, 1, 2]
b = [2, 1, 1]
c = ['a', 'b', 'c']
d = zip(a, b, c)
d = sorted(d, key=lambda x: [x[0], x[1]], reverse=True)
a, b, c = map(list, zip(*d))
print(a, b, c)


# argsort（ソート後の元々の index）
def get_sorted_and_argsort_index(L, reverse=False):
    R = list(range(len(L)))
    Z = zip(L, R)
    Z = sorted(Z, key=lambda x: x[0], reverse=reverse)
    L, R = map(list, zip(*Z))
    return L, R


L = [1, 3, 2, 4, 5]
L, I = get_sorted_and_argsort_index(L, reverse=True)

print(L, I) #=> [5, 4, 3, 2, 1] [4, 3, 1, 2, 0]


# 各数字が何番目に大きいか
def get_sorted_and_argsort_index(L, reverse=False):
    R = list(range(len(L)))
    Z = zip(L, R)
    Z = sorted(Z, key=lambda x: x[0], reverse=reverse)
    L, R = map(list, zip(*Z))
    return L, R


P = [12, 11, 13]
P, Q = get_sorted_and_argsort_index(P, reverse=True)
Q, R = get_sorted_and_argsort_index(Q, reverse=False)

for r in R:
    print(r + 1)


# 多次元配列の平滑化（flatten）, 内包表記より高速らしい
from itertools import chain


P = [[1, 2], [3]]
P = list(chain.from_iterable(P))
print(P) #=> [1, 2, 3]


# 内包表記の途中中断 break
list(x if x < 10 else next(iter([])) for x in range(100)) #=> [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


# 素因数分解、約数列挙
def get_prime_factorized(N):
    R = []
    b, e = 2, 0
    while b ** 2 <= N:
        while N % b == 0:
            N  = N // b
            e += 1
        if e > 0:
            R.append([b, e])
        b, e = b + 1, 0
    if N > 1:
        R.append([N, 1])
    return R

def get_list_divisor(N, reverse=True):
    try:
        F = get_prime_factorized(N)
        L = re_func_divisior(F)
        R = []
        for l in L:
            for i, x in enumerate(l):
                if i == 0:
                    r = x
                else:
                    r *= x
            R.append(r)
        R.sort()
        if reverse == True:
            R.reverse()
    except:
        if N == 1:
            R = [1]
        else:
            R = [N]
    return R

def re_func_divisior(F):
    b, e = F.pop()
    P = re_func_divisior(F) if F else [[]]
    Q = [[b ** k] for k in range(e + 1)]
    return [p + q for p in P for q in Q]


get_prime_factorized(24) #=> [[2, 3], [3, 1]]
get_list_divisor(24)     #=> [24, 12, 8, 6, 4, 3, 2, 1]


# 素数関連
def get_list_primes(N):
    if N < 1:
        return []
    else:
        sqrt_N = int(N ** 0.5)
        P = [i for i in range(N + 1)]
        for p in P:
            if p == 0:
                continue
            elif p > sqrt_N:
                break
            else:
                for np in range(2 * prime, N + 1, prime):
                    P[np] = 0
        return [p for p in P if p != 0][1:]


get_list_primes(11) #=> [2, 3, 5, 7, 9, 11]
N = 11
L = get_list_primes(N)
N == L[-1] #=> True, 11 is prime

# 最大公約数
def get_gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


# 最小公倍数
def get_lcm(a, b, gcd=0):
    if gcd == 0:
        return a * b // get_gcd(a, b)
    else:
        return a * b // gcd


# 正規表現
import re


if re.match(r'\d{%d}-\d{%d}' % (3, 4), '123-4567'):
    print('Yes')
else:
    print('No')


# 文字列の定型リスト
import string


a_z = list(string.ascii_lowercase)
A_Z = list(string.ascii_uppercase)
a_Z = list(string.ascii_letters)
0_9 = list(string.digits)
0_F = list(string.hexdigits)


# 無向グラフの読み込み
# 点の数(N, index は 0 から N-1)、辺の数(N-1)
# 点A から点B までのコストC（a, b, c）
N = int(input())
H = {}

for n in range(N):
    H[n] = []

for n in range(N-1):
    a, b, c = map(int, input().split())
    H[a].append([b, c])
    H[b].append([a, c])

# 上記の無向グラフの根を K とした木のコストリスト作成（ABC070 D）
# index 0- の sample
'''
5
0 1 1
0 2 1
1 3 1
2 4 1
2 0
'''
Q, K = map(int, input().split())
C    = [0]    * N
F    = [True] * N
C[K] = 0
F[K] = False

L = [K]

while len(L) > 0:
    L_tmp = []
    for k in L:
        for t in H[k]:
            b, c = t
            if F[b] == True:
                C[b] = C[k] + c
                F[b] = False
                L_tmp.append(b)
    L = L_tmp

print(C)


# 多重リストのコピーは copy.deepcopy()
import copy


N = 100
S = [[None for r in range(N)] for l in range(N)]

for i in range(N):
    S[i][i] = A[i]

X = copy.deepcopy(S)


# 中央値（中央値風の中央値より小さい値）
import statistics


A = [1, 2, 3, 4]
M = int(statistics.median(A))


# math ライブラリは python 3.4 で math.ord() 使えない

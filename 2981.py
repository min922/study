# https://www.acmicpc.net/problem/2981
import math
import sys

N = int(sys.stdin.readline().strip())
num = []
bound = 1e9
for i in range(N):
    num.append(int(sys.stdin.readline().strip()))

gcdnum = 0
for i in range(N - 1):
    tmp = num[i + 1] - num[i]  # A = M*a+r, B = M*b+r, C = M*c+r => gcd(B-A, C-B) = M 일때 나머지 같음
    gcdnum = math.gcd(tmp, gcdnum)
gcdlist = {gcdnum}

for i in range(2, int(math.sqrt(gcdnum)) + 1):  # EX)12라면 1&12/2&6/3&4 한 번에 추가
    if gcdnum % i == 0:
        gcdlist.add(i)
        gcdlist.add(gcdnum // i)

gcdlist = list(gcdlist)  # 정렬 위해 리스트로
gcdlist.sort()
for gcd in gcdlist:
    print(gcd, end=' ')

# 시간 초과
# for i in range(2, bound):
#     mod = set()
#     for n in num:
#         mod.add(n % i)
#     if len(mod) == 1: # 나머지가 모두 같을 때
#         print(i, end=' ')

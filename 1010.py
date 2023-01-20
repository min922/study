# https://www.acmicpc.net/problem/1010
import sys, math


def nCr(n, r):
    return math.factorial(n) // (math.factorial(r) * math.factorial(n - r))


T = int(sys.stdin.readline().strip())
testcase = []
for i in range(T):
    testcase.append(list(map(int, sys.stdin.readline().split())))

for case in testcase:
    print(nCr(case[1], case[0]))

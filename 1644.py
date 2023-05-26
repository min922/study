# https://www.acmicpc.net/problem/1644
import sys


def seive(p):
    primelist = []
    rnum = [False, False] + [True] * (p - 1)
    for i in range(1, p + 1):
        if rnum[i]:
            primelist.append(i)
            for j in range(2 * i, p + 1, i):
                rnum[j] = False
    return primelist


n = int(sys.stdin.readline().strip())
prime = seive(n)
left, right = 0, 0
result = 0
while right <= len(prime):
    tmp = sum(prime[left:right])
    if tmp == n:
        result += 1
        right += 1
    elif tmp < n:
        right += 1
    else:
        left += 1
print(result)

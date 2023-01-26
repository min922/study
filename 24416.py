# https://www.acmicpc.net/problem/24416
import sys


def fib(n):
    global cnt1
    if n == 1 or n == 2:
        cnt1 += 1
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


def fibonacci(n):
    global cnt2
    f = [0 for _ in range(n)]
    f[0] = 1
    f[1] = f[0]
    for i in range(2, n):
        cnt2 += 1
        f[i] = f[i - 1] + f[i - 2]
    return f[-1]


n = int(sys.stdin.readline().strip())
cnt1, cnt2 = 0, 0
fib(n)
fibonacci(n)
print(cnt1, cnt2)

# 재귀이기때문에 Python3으로 제출하니 시간초과, PyPy3으로 하니 통과

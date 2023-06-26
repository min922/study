# https://www.acmicpc.net/problem/17386
import sys

x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
x3, y3, x4, y4 = map(int, sys.stdin.readline().split())

P, Q, R, S = [x1, y1], [x2, y2], [x3, y3], [x4, y4]


def CCW(A, B, C):
    return (A[0] * B[1] + B[0] * C[1] + C[0] * A[1]) - (A[1] * B[0] + B[1] * C[0] + C[1] * A[0])


if CCW(P, Q, R) * CCW(P, Q, S) < 0 and CCW(R, S, P) * CCW(R, S, Q) < 0:
    print(1)
else:
    print(0)

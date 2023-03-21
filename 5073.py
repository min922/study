# https://www.acmicpc.net/problem/5073
import sys

while True:
    seg = list(map(int, sys.stdin.readline().split()))
    seg.sort()
    a, b, c = seg[0], seg[1], seg[2]  # 오름차순 정렬
    if a == 0 and b == 0 and c == 0:
        break
    else:
        if c >= a + b:
            print("Invalid")
        elif a == b and b == c and c == a:
            print("Equilateral")
        elif a == b or b == c or c == a:
            print("Isosceles")
        else:
            print("Scalene")

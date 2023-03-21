# https://www.acmicpc.net/problem/15894
import sys

n = int(sys.stdin.readline().strip())

print(2 * n * (n + 1) - 2 * n * (n - 1))
# 전체 정사각형의 둘레 - 겹치는 부분

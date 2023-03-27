# https://www.acmicpc.net/problem/13909
import sys

n = int(sys.stdin.readline().strip())

print(int(n ** 0.5))

# n = 3 -> 111 / 101 / 100
# n = 4 -> 1111 / 1010 / 1000 / 1001
# n = 5 -> 11111 / 10101 / 10001 / 10011 / 10010
# n = 6 -> 111111 / 101010 / 100011 / 100111 / 100101 / 100100
# 제곱수번째만 열려있음

# https://www.acmicpc.net/problem/2609
def gcd(a, b):
    for cd in range(min(a, b), 0, -1): # 크기 큰 순으로
        if a % cd == 0 and b % cd == 0: # common divisor가 a와 b 모두 나눌 때
            return cd

def lcm(a, b):
    for cm in range(max(a, b), a * b + 1): 
        if cm % a == 0 and cm % b == 0: # common multiple이 a로도 b로도 나누어떨어질 때
            return cm

import sys
a, b = map(int, sys.stdin.readline().split())
print(gcd(a, b))
print(lcm(a, b))

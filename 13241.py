# https://www.acmicpc.net/problem/13241
import sys


def euclid(a, b):
    multi = a * b
    while b != 0:
        r = a % b
        a = b
        b = r
    return multi // a  # lcm(a, b) = a*b//gcd(a, b)


a, b = map(int, sys.stdin.readline().split())
print(euclid(a, b))

# https://www.acmicpc.net/problem/1735
import sys


def euclidgcd(a, b):
    multi = a * b
    while b != 0:
        r = a % b
        a = b
        b = r
    return a


x, y = map(int, sys.stdin.readline().split())
w, z = map(int, sys.stdin.readline().split())

lcm = (y * z) // euclidgcd(y, z)
mole_1 = x * (lcm // y)
mole_2 = w * (lcm // z)
mole = mole_1 + mole_2

gcd = euclidgcd(mole, lcm)
print(mole // gcd, lcm // gcd)

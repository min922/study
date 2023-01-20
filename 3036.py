# https://www.acmicpc.net/problem/3036
import sys, math

N = int(sys.stdin.readline().strip())
data = list(map(int, sys.stdin.readline().split()))

for i in range(1, len(data)):
    gcd = math.gcd(data[0], data[i])
    print(str(data[0] // gcd) + "/" + str(data[i] // gcd))

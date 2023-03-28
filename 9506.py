# https://www.acmicpc.net/problem/9506
import sys

while True:
    n = int(sys.stdin.readline().strip())
    if n == -1:
        break
    else:
        cnt = 0
        numlist = []
        for i in range(1, n):
            if n % i == 0:
                numlist.append(i)
                cnt += i
        if cnt != n:
            print(n, "is NOT perfect.")
        else:
            print(n, " = ", " + ".join(str(i) for i in numlist), sep="")

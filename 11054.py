# https://www.acmicpc.net/problem/11054
import sys

n = int(sys.stdin.readline().strip())

seq = list(map(int, sys.stdin.readline().split()))
seq_rev = list(reversed(seq))  # 감소하는 수열 구하기 위해

inc = [0 for _ in range(n)]
dec = [0 for _ in range(n)]
for i in range(n):
    for j in range(i):
        if seq[i] > seq[j] and inc[i] < inc[j]:  # seq가 증가하고 부분수열의 크기가 최대가 아닐 때
            inc[i] = inc[j]
        if seq_rev[i] > seq_rev[j] and dec[i] < dec[j]:  # seq가 감소하고 부분수열의 크기가 최대가 아닐 때
            dec[i] = dec[j]
    inc[i] += 1  # seq[i]까지 포함하니까 1 증가
    dec[i] += 1
dec.reverse()

dp = [inc[i] + dec[i] - 1 for i in range(n)]  # 바이토닉 수열 구하기 위해 ex)123(증가)+32(감소) -> 1232(바이토닉)
print(max(dp))

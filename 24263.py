# https://www.acmicpc.net/problem/24263
import sys

n = int(sys.stdin.readline().strip())

# MenOfPassion(A[], n) {
#     sum <- 0;
#     for i <- 1 to n
#         sum <- sum + A[i]; # 코드1
#     return sum;
# }
# -> i가 1부터 n까지일때를 반복 : O(n)의 시간복잡도

print(n)  # 수행횟수 : 1부터 n까지 반복문
print(1)  # O(n) -> 차수 1

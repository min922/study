# https://www.acmicpc.net/problem/24266
import sys

n = int(sys.stdin.readline().strip())

# MenOfPassion(A[], n) {
#     sum <- 0;
#     for i <- 1 to n
#         for j <- 1 to n
#             for k <- 1 to n
#                 sum <- sum + A[i] × A[j] × A[k]; # 코드1
#     return sum;
# }
# -> 반복문 3번 중첩 -> O(n^3)의 시간복잡도

print(n**3)  # 수행횟수 : 1~n까지가 3번 반복
print(3)  # O(n^3) -> 차수 3

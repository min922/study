# https://www.acmicpc.net/problem/24265
import sys

n = int(sys.stdin.readline().strip())

# MenOfPassion(A[], n) {
#     sum <- 0;
#     for i <- 1 to n - 1
#         for j <- i + 1 to n
#             sum <- sum + A[i] × A[j]; # 코드1
#     return sum;
# }
# -> 반복문 2번 중첩 -> O(n^2)의 시간복잡도

print(n * (n - 1) // 2)  # 수행횟수 : i는 1~n-1, j는 i+1~n -> n-1부터 1까지의 합 만큼 반복
print(2)  # O(n^2) -> 차수 2

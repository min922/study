# https://www.acmicpc.net/problem/24267
import sys

n = int(sys.stdin.readline().strip())

# MenOfPassion(A[], n) {
#     sum <- 0;
#     for i <- 1 to n - 2
#         for j <- i + 1 to n - 1
#             for k <- j + 1 to n
#                 sum <- sum + A[i] × A[j] × A[k]; # 코드1
#     return sum;
# }
# -> 반복문 3번 중첩 -> O(n^3)의 시간복잡도

print(((n - 1) * (n - 2) * (2 * n - 3) + 3 * (n - 1) * (n - 2)) // 12)  # 수행횟수 : i:1~n-2, j:i+1~n-1, k:j+1~n
print(3)  # O(n^3) -> 차수 3

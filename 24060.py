# https://www.acmicpc.net/problem/24060
import sys

def merge_sort(sort_list): # sort_list를 오름차순 정렬
    n = len(sort_list)
    if n <= 1:
        return
    mid = (n + 1) // 2
    left = sort_list[:mid]
    right = sort_list[mid:]
    merge_sort(left) # 앞쪽 정렬
    merge_sort(right) # 뒷쪽 정렬
    merge(sort_list, left, right) # 정렬 후 병합
    return sort_list


def merge(sort_list, left, right): # 앞쪽 뒷쪽 하나씩 뽑아와서 비교해서 정렬
    i1 = 0; i2 = 0; i_sort = 0
    while i1 < len(left) and i2 < len(right):
        if left[i1] < right[i2]:
            sort_list[i_sort] = left[i1]
            ans.append(left[i1])
            i1 += 1; i_sort += 1
        else:
            sort_list[i_sort] = right[i2]
            ans.append(right[i2])
            i2 += 1; i_sort += 1
    while i1 < len(left): # 앞쪽 남았을 때
        sort_list[i_sort] = left[i1]
        ans.append(left[i1])
        i1 += 1; i_sort += 1
    while i2 < len(right): # 뒷쪽 남았을 때
        sort_list[i_sort] = right[i2]
        ans.append(right[i2])
        i2 += 1; i_sort += 1

n, k = map(int, sys.stdin.readline().split())
a = list(map(int, sys.stdin.readline().split()))
ans = []
merge_sort(a)
if len(ans) >= k:
    print(ans[k-1])
else:
    print(-1)

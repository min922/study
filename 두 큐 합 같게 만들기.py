def solution(queue1, queue2):
    sum1 = sum(queue1) 
    sum2 = sum(queue2)
    # sum은 O(n)의 복잡도 -> 변수에 저장하면 O(1)로 사용가능
    all_queue = queue1 + queue2 #앞에서 부터 붙히니까

    i, j = 0, len(queue1) #q1, q2 나누는 포인터
    cnt = 0
    while (i < len(all_queue) and (j < len(all_queue))):
        if sum1 > sum2:
            sum1 -= all_queue[i]
            sum2 += all_queue[i]
            cnt += 1
            i += 1
        elif sum1 < sum2:
            sum1 += all_queue[j]
            sum2 -= all_queue[j]
            cnt += 1
            j += 1
        else:
            return cnt
    return -1

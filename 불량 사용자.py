import re
from itertools import *

def solution(user_id, banned_id):
    answer = []
    banned_id = [i.replace("*", ".") for i in banned_id] #정규표현식으로 바꿈
    result = []
    id_list = list(permutations(user_id, len(banned_id))) #제재가 될수있는 모든 조합

    for id in id_list:
        tmp = set()
        for idx, bid in enumerate(banned_id):
            p = re.compile(bid)
            m = p.match(id[idx])
            if m and len(bid) == len(id[idx]): #제재아이디와 같으면 add
                tmp.add(id[idx])
        if len(tmp) == len(id): #조합의 모든 id가 제재아이디와 같으면 append
            result.append(set(list(id)))

    for idx, r in enumerate(result): #중복제거
        if r not in result[idx+1:]:
            answer.append(r)

    return len(answer)

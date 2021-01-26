import itertools  # 항상 정렬 주의할것, 단순히 정답을 맞추는 것 보단 비효율성이 어디에 숨어있는지 체크하기
def solution(o,c):
    answer = []

    p = [sorted(list(i)) for i in o]
    for i in c:
        dic = {}
        for j in p:
            a = itertools.combinations(j,i)
            for k in a:
                if ''.join(k) in dic:
                    dic[''.join(k)] += 1
                else:
                    dic[''.join(k)] = 1
        if dic != {} and max(dic.values()) != 1:
            answer.extend([k for k,v in dic.items() if v == max(dic.values())])
    answer.sort()
    return answer
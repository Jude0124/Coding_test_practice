def solution(a, b):
    answer = 0
    for c,d in zip(a,b):
        answer +=c*d
    return answer
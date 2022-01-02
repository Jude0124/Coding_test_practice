def solution(a,s):
    answer = 0
    for i,j in zip(a,s):
        if j: answer += i
        else: answer -= i
    return answer
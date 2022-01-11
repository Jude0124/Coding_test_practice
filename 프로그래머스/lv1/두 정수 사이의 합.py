def solution(a, b):
    answer = 0
    if a == b :
        answer = a
    elif a > b :
        answer = sum(x for x in range(b,a+1))
    else:
        answer = sum(x for x in range(a,b+1))
    return answer
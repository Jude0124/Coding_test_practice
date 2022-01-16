def solution(left, right):
    answer = 0
    while left <= right:
        if left**(1/2)-int(left**(1/2)): answer += left          
        else : answer -= left
        left += 1
    return answer
def solution(n, k):
    t = ""
    while k != 0:
        if n == "":
            t = t[:-k]
            k = 0
            break
        if t == "":
            t += n[0]
            n = n[1:]
        else:
            if t[-1] < n[0]:
                t = t[:-1]
                k -= 1
            else:
                t += n[0]
                n = n[1:]           
    return t+n

# 테케 규모가 커진것에 대해서 함부로 string to list 하지 말것. 
# str 그대로 푸는 것이 연산 효율성 더 좋은듯.
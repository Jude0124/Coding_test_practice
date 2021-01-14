def solution(s):
    answer = ""
    for k,v in enumerate(s):
        if k == 0:
            answer += v.upper()
        elif answer[k-1].isupper():
            answer += v.lower()
        else:
            answer += v.upper()
    return answer

# 리스트 컴프리핸션을 이용한 한줄풀이
# 리스트 컴프리핸션 내에서 이중 포문을 어떻게 사용하는지 몰라 구글링 후 완.

# def solution(s):
#     return ' '.join([''.join([v.upper() if k % 2 == 0 else v.lower() for k, v in enumerate(o)]) for o in s.split(" ")])
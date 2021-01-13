def solution(arr):
    if len(arr) == 1:
        return [-1]
    else:
        arr.remove(min(arr))
        return arr
#리스트 컴프리핸션 이용
# 정확성은 똑같지만 루프를 돌아야하므로 효율성 down...비추
# return [i for i in arr if i> min(arr)] or [-1]
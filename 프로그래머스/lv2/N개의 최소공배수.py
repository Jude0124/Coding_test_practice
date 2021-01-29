def solution(a):
    while len(a) != 1:
        b,c = max(a[0],a[1]),min(a[0],a[1])
        while c != 0:
            d = b%c
            b,c = c,d
        a[1] = a[0]*a[1]/b
        a.pop(0)
    return a[0]
#유클리드 호제법 배열 길이가 1 일때까지 반복

def solution(w,h):
    a = max([w,h])
    b = min([w,h])
    for i in range(b,0,-1):
        if a%i==0 and b%i ==0 :
            c = i
            break
    return a*(b-1)-b+c
def solution(n):
    c = 0 
    p = 1
    while n != 0:
        t = c
        c += p
        p = t
        n -= 1
    return c%1234567
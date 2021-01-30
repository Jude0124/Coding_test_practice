def solution(n):
    k = n+1
    c = bin(n).count("1")
    while bin(k).count("1") !=c:
        k += 1
    return k
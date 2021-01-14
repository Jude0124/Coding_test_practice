def solution(n):
    return n[-4:].rjust(len(n),"*")
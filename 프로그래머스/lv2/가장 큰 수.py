def solution(n):
    return str(int("".join(sorted(map(str,n),key= lambda x : (x*4),reverse = True))))
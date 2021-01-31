def solution(s):
    c = 0
    for i in range(len(s)):
        if s[i] == "(":
            c += 1
        else:
            c -= 1
        if c < 0:
            return False
    if c == 0:    
        return True
    return False
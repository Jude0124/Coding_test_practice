def solution(n,s,w):
    base,cnt = 1,0
    while s != []:
        now = s.pop(0)
        if base < now-w:
            cnt += (now - base + w)//(2*w+1)
        base = now+w+1
        if (s == []) and (n > now+w):
            cnt += (n - now + w)//(2*w+1)
    return cnt
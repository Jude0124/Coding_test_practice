def solution(n,s,w):
    base,cnt = 1,0
    while s != []:
        now = s.pop(0)
        if base < now-w:
            cnt += (now - base + w)//(2*w+1)
        base = now+w+1    
    if n > now+w:
        cnt += (n - now + w)//(2*w+1)
    return cnt
    
# 최소 하나의 기지국은 설치되어 있기때문에 기지국들 사이에 빈공간에 필요한 최소한의 기지국 갯수를 모두 더해주어 출력
# 수정사항 마지막 if문 while문 밖에서 처리해주어 효율성 up

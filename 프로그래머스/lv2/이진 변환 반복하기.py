def solution(s):
    cnt0 = 0
    cnt =0
    while s !='1':
        cnt+=1
        pre = len(s)
        s = s.replace("0","")
        now = len(s)
        cnt0 += (pre-now)
        i = 1
        while len(s) >= i:
            i *= 2
        i /=2
        k = len(s)
        b = ''
        while i != 1/2:
            b += str(int(k//i))
            k -= (k//i)*i
            i /=2
        s = b
    return [cnt,cnt0]



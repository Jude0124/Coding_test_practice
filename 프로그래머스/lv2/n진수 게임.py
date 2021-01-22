def solution(n, t, m, p):
    b = "0"
    num = 1
    cnt = 1
    while len(b)<t*m:
        cnt += 1
        c = ""
        while num>0:        
            if num%n in [10,11,12,13,14,15]:
                c += str(["A","B","C","D","E","F"][num%n-10])
            else:
                c += str(num%n)
            num = num//n
        c = c[::-1]
        b += c
        num = cnt    
    
    answer = ''
    for i in range(t):
        answer += b[i*m+p-1]

    return answer
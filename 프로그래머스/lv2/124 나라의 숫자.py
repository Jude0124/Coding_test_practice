def solution(n):
    answer = []
    
    while n != 0 :
        if n%3 == 0:
            answer.append('4')
            n -= 3
        elif n%3 == 1:
            answer.append('1')
        else:
            answer.append('2')
        n -= n%3
        n /= 3
        
    return "".join(reversed(answer))
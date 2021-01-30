def solution(n):
    cnt = 1
    for i in range(2,n):
        if n < i*(i+1)/2:
            break
        if (n-i*(i+1)/2)%i == 0:
            cnt += 1
    return cnt

# 다른사람 풀이
def expressions(num):
    return len([i  for i in range(1,num+1,2) if num % i == 0])

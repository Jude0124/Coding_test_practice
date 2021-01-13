def solution(n):
    cnt = [True]*n
    
    for i in range(2,int(n/2)+1):
        if (cnt[i-1] == True):
            for j in range(i*2,n+1,i):
                cnt[j-1] = False
                
    return cnt.count(True)-1

# 다른 사람의 풀이
# def solution(n):
#     num=set(range(2,n+1))

#     for i in range(2,n+1):
#         if i in num:
#             num-=set(range(2*i,n+1,i))
#     return len(num)


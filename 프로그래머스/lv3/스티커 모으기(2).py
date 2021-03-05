def solution(s):
    if len(s) == 1 : return s[0] # 리스트 길이가 하나인 경우 iter를 돌지 않는 것 방지
    dp1 = [0,0]
    for i in s[1:]:
        dp1 = [max(dp1),dp1[0]+i]
        
    dp2 = [0,0]
    for j in s[:-1]:
        dp2 = [max(dp2),dp2[0]+j]
    
    return max(dp1+dp2)

# dp 문제 
# dp[0] == 두시점 이전까지의 최댓값, i == 현재 값
# 한시점 이전의 값보다 두시점 이전의 값 + i 가 더 크면 해당 값 선택
# 두시점 이전의 값에 대하여 한시점 이전을 더한 값이 더 크면 max(dp[0]) 선택
# 추후 복습 必
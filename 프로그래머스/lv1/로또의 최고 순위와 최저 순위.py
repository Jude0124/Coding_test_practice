def solution(lottos, win_nums):
    cnt1,cnt2 = 0,0
    rank = [6,6,5,4,3,2,1]
    for i in lottos:
        if i in win_nums:
            cnt1 += 1
        elif i == 0:
            cnt2 += 1
    return [rank[cnt1+cnt2],rank[cnt1]]
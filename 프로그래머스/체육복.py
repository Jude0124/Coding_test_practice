def solution(n, lost, reserve):
    ans = set()
    res = set(reserve)-set(lost) 
    los = set(lost)-set(reserve) 
    cnt = 0
    for i in los: 
        if i-1 in res: 
            cnt+=1
        elif i+1 in res: 
            cnt+=1
            res.remove(i+1)
            
    return n-len(los)+cnt

    # 깨달은점 1 
    # 반복문에서는 iter를 도는 동안 반복되는 집합이 변경되어서는 안된다-> cnt 변수로 해결
    # 깨달은점 2
    # 반복문은 리스트의 앞에서부터 차례로 탐색하므로, 조건절 내에서 여벌이 있는 사람의 경우도  앞사람 부터 탐색을 하며,
    # 뒷뒷사람과 나 자신이 뒷사람의 체육복이 모두 필요하지만 뒷뒷사람의 경우 뒷뒷뒷사람 또한 여벌이 있어 ,
    # 나 자신과 뒷뒷사람  모두 각자의 뒷사람에게서 체육복을 빌릴 수 있는 경우를 catch하지 못하게 된다.
    # 이를  각자의 iter에서 앞사람이 아닌 뒷사람에게 빌렸을 경우 해당 여벌이 있는 사람을 아예 set에서 remove하여 해당 문제를 보완할 수 있다.
    
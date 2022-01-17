def solution(id_list, report, k):
    report_log  , answer , report = dict() , [] , list(set(report))
    # key = 사용자 아이디 , value = [value1, [value2]]
    # value1 = 사용자가 신고 받은 횟수 / value2 = 사용자가 신고한 사람 목록


    for key in id_list:                         # 딕셔너리 생성
        report_log[key] = [0,[]]
    
    for repo in report:                         # 신고한 사람 목록과 횟수 기입
        temp = repo.split()
        report_log[temp[0]][1].append(temp[1])
        report_log[temp[1]][0] += 1
    
    for key in id_list:                         # 조회하면서 해당 사용자가 받아야할 메일 수 산출 
        cnt = 0
        for value2 in report_log[key][1]:
            if report_log[value2][0] >= k:
                cnt += 1             
        answer.append(cnt)
    
    return answer
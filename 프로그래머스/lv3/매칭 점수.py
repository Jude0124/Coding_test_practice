import re
def solution(w,p):
    w = w.lower()
    base_score,exurl, url = [],[],[]
    for i in range(len(p)):
        p[i] = p[i].lower()    
        url.append(re.search(r'<meta property=\"og:url\" content=\"https://([\S]*)\"/>',p[i]).group(1))
        base_score.append(re.findall(r'[a-z]+',p[i]).count(w))    
        exurl.append(list(set(re.findall(r'<a href="https://([\S]+)">',p[i]))))
        
    match_score = base_score[:]
    
    for  i in range(len(p)):
        for j in range(len(p)):
                if (i != j) and (url[i] in exurl[j]):
                        match_score[i] += base_score[j]/len(exurl[j])
                        
    return match_score.index(max(match_score))

# 정규식 .* 쓰지말것 [\S] 으로 링크를 찾는 것이 무조건 정확하다. 주소에는 공백이 올수 없다.
#  search findall match group 

# 리스트 보다는 딕셔너리 형식으로 깔끔하게 정리하는 습관들이기 
# base_score == 기본점수 ,exurl == 외부 링크 목록, url == 해당 사이트 주소(index역할)

# 시간 잡아먹었던 구간 
# 따로 외부링크 목록을 list로 빼는게 귀찮아서 안잡아주고 raw_file에서 외부링크 수를 탐색해서 자꾸 틀렸다.
# 외부링크는 반드시 a href 형식을 지키고 있지만, raw_file에서 탐색하면 해당 찾고자하는 url이 다른 태그에도 존재할 수 있어서
# 갯수를 정확히 셀 수 없다. + set 연산 반드시 해주어야함 특정 링크가 10번 언급되어도 링크는 1번으로 인식해야 하는것이  맞다.